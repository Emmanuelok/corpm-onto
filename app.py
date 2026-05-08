from __future__ import annotations

from http import HTTPStatus
from mimetypes import guess_type
from pathlib import Path
from typing import Callable, Iterable
from urllib.parse import unquote

SITE_DIR = Path(__file__).resolve().parent / "site"
StartResponse = Callable[[str, list[tuple[str, str]]], object]
WsgiApp = Callable[[dict[str, str], StartResponse], Iterable[bytes]]


def _is_relative_to(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def resolve_site_path(path_info: str, site_dir: Path = SITE_DIR) -> Path | None:
    """Resolve a request path to a built MkDocs static file."""
    site_root = site_dir.resolve()
    requested = unquote(path_info or "/").lstrip("/")
    candidate = (site_root / requested).resolve()

    if not _is_relative_to(candidate, site_root):
        return None

    candidates = [candidate]
    if path_info.endswith("/") or not candidate.suffix:
        candidates.append(candidate / "index.html")
    if not requested:
        candidates.append(site_root / "index.html")

    for possible_file in candidates:
        if _is_relative_to(possible_file.resolve(), site_root) and possible_file.is_file():
            return possible_file

    return None


def make_wsgi_app(site_dir: Path = SITE_DIR) -> WsgiApp:
    """Create a minimal WSGI app that serves the built documentation site."""

    def static_docs_app(environ: dict[str, str], start_response: StartResponse) -> Iterable[bytes]:
        method = environ.get("REQUEST_METHOD", "GET").upper()
        if method not in {"GET", "HEAD"}:
            status = HTTPStatus.METHOD_NOT_ALLOWED
            start_response(
                f"{status.value} {status.phrase}",
                [("Content-Type", "text/plain; charset=utf-8"), ("Allow", "GET, HEAD")],
            )
            return [b""]

        file_path = resolve_site_path(environ.get("PATH_INFO", "/"), site_dir)
        status = HTTPStatus.OK
        if file_path is None:
            file_path = resolve_site_path("/404.html", site_dir)
            status = HTTPStatus.NOT_FOUND

        if file_path is None:
            start_response(
                f"{status.value} {status.phrase}",
                [("Content-Type", "text/plain; charset=utf-8")],
            )
            return [b"404 Not Found"] if method == "GET" else [b""]

        content_type, encoding = guess_type(file_path.name)
        headers = [("Content-Type", content_type or "application/octet-stream")]
        if encoding:
            headers.append(("Content-Encoding", encoding))
        start_response(f"{status.value} {status.phrase}", headers)
        return [file_path.read_bytes()] if method == "GET" else [b""]

    return static_docs_app


app = make_wsgi_app()
