import click


@click.option("--version", required=True)
@click.command()
def main(version):
    with open("pyproject.toml", "r") as f:
        lines = f.readlines()
    with open("pyproject.toml", "w") as f:
        for line in lines:
            if line.startswith("version"):
                line = f'version = "{version}"\n'
            f.write(line)
    with open(".conda/meta.yaml", "r") as f:
        lines = list(f.readlines())
    lines[0] = f'{{% set version = "{version}" %}}\n'
    with open(".conda/meta.yaml", "w") as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    main()
