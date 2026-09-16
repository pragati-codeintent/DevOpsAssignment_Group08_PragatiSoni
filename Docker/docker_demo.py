# Simple Docker Demo Program

project_name = "DevOps Assignment"
docker_version = "Docker 1.0"
container_name = "demo-container"

print("================================")
print("       DOCKER DEMO PROGRAM")
print("================================")

print("Project Name:", project_name)
print("Docker Version:", docker_version)
print("Container Name:", container_name)

print()
print("Docker is a containerization platform.")
print("It helps package applications.")
print("A Docker image contains application files.")
print("A container runs an image.")
print("Containers are isolated from each other.")

print()
print("Starting application...")

status = "Running"

print("Container Status:", status)
print("Checking application...")

application_name = "Python Application"
application_port = 5000

print("Application:", application_name)
print("Port:", application_port)

print()
print("Performing basic checks...")

check_1 = True
check_2 = True
check_3 = True
check_4 = True

print("Python check:", check_1)
print("Docker check:", check_2)
print("Network check:", check_3)
print("Application check:", check_4)

print()
print("All basic checks completed.")

if check_1 and check_2 and check_3 and check_4:
    print("Application is ready.")
else:
    print("Application needs attention.")

print()
print("Container information:")
print("Name:", container_name)
print("Status:", status)
print("Application:", application_name)
print("Port:", application_port)

print()
print("Docker demo completed successfully.")
print("================================")