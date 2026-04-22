from corruptpm.validate import validate_project


def main() -> None:
    result = validate_project()
    print(result.report_text.strip())
    raise SystemExit(0 if result.conforms else 1)


if __name__ == "__main__":
    main()

