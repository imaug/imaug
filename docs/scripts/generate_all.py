from pathlib import Path
import subprocess

def main():
    print(Path(__file__))
    for script in sorted(Path(__file__).parent.glob('**/*.py')):
        if not script.name in [
            "generate_all.py",
            "utils.py", # images_documentation/utils.py
            #"a_measure_performance.py", # Rather time consuming
        ]:
            cmd = ["python", str(script)]
            print(' '.join(cmd))
            assert subprocess.run(cmd).returncode == 0

if __name__ == '__main__':
    main()