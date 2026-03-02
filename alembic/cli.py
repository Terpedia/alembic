"""CLI entry point."""

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m alembic <prompt>", file=sys.stderr)
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])
    from alembic import VertexClient
    client = VertexClient()
    try:
        print(client.generate(prompt))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
