import subprocess

def run_tests():
    try:
        subprocess.run(['python', '-m', 'unittest', 'discover', '-s', 'tests', '-v'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")
        exit(1)

if __name__ == '__main__':
    run_tests()
