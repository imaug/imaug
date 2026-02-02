from argparse import ArgumentParser
from pathlib import Path
import subprocess

def main():
    parser = ArgumentParser()
    parser.add_argument('--all', action="store_true")
    args = parser.parse_args()

    print(Path(__file__))
    exclude_list = [
        "generate_all.py",
        "utils.py", # images_documentation/utils.py
    ]
    if not args.all:
        exclude_list += [
            "a_measure_performance.py", # Rather time consuming
            "b_convert_performance_measurements_to_tables.py", # Depends on previous step
        ]

    for script in sorted(Path(__file__).parent.glob('**/*.py')):
        if not script.name in exclude_list:
            cmd = ["python", str(script)]
            print(' '.join(cmd))
            assert subprocess.run(cmd).returncode == 0

if __name__ == '__main__':
    main()