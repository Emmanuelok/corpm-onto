from __future__ import annotations

from pathlib import Path

from app import make_wsgi_app, resolve_site_path


def _call_app(site_dir: Path, path_info: str, method: str = "GET") -> tuple[str, list[tuple[str, str]], bytes]:
    status_headers: dict[str, object] = {}

    def start_response(status: str, headers: list[tuple[str, str]]) -> None:
        status_headers["status"] = status
        status_headers["headers"] = headers

    body = b"".join(make_wsgi_app(site_dir)({"PATH_INFO": path_info, "REQUEST_METHOD": method}, start_response))
    return status_headers["status"], status_headers["headers"], body


def test_resolve_site_path_serves_mkdocs_clean_urls(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text("home", encoding="utf-8")
    guide_dir = tmp_path / "getting-started"
    guide_dir.mkdir()
    (guide_dir / "index.html").write_text("guide", encoding="utf-8")

    assert resolve_site_path("/", tmp_path) == tmp_path / "index.html"
    assert resolve_site_path("/getting-started", tmp_path) == guide_dir / "index.html"


def test_resolve_site_path_rejects_path_traversal(tmp_path: Path) -> None:
    assert resolve_site_path("/../pyproject.toml", tmp_path) is None


def test_wsgi_app_serves_static_file_and_404(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text("home", encoding="utf-8")
    (tmp_path / "404.html").write_text("missing", encoding="utf-8")

    status, headers, body = _call_app(tmp_path, "/")
    assert status == "200 OK"
    assert ("Content-Type", "text/html") in headers
    assert body == b"home"

    status, _, body = _call_app(tmp_path, "/missing-page")
    assert status == "404 Not Found"
    assert body == b"missing"
