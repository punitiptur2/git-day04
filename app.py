import subprocess

command = [
    "eksctl", "create", "cluster",
    "--name", "test",
    "--region", "us-east-1",
    "--node-type", "t2.medium",
    "--nodes", "7"
]

subprocess.run(command, check=True)
