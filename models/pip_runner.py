def run_pip(pip_commands):
    import subprocess
    for command in pip_commands:
        try:
            subprocess.check_call([command])
        except subprocess.CalledProcessError as e:
            print(f"Error running pip command: {e}")
            return False
    return True