Setup Guide: Python Development Environment with Nexus Integration

This guide outlines the prerequisites and step-by-step instructions for setting up a Python development environment with Nexus integration, including Java, Poetry, Hadoop, and PyCharm configuration.

Prerequisites

Before proceeding, ensure the following requirements are met:
	1.	Nexus Access:
	•	Obtain access to your Nexus repository from your organization.
	•	Ensure you have the repository URL (e.g., https://nexus.example.com/repository/pypi-all).
	2.	Obtain Tokens:
	•	Retrieve your Nexus authentication tokens (username and passcode).
	•	If the repository uses SSL, ensure you can access the required certificates.
	3.	Install Python:
	•	Download and install Python 3.9 or higher from python.org.
	•	Add Python to your system PATH during installation.
Verify installation:

python --version


	4.	Install Java:
	•	Download and install Java Development Kit (JDK) 8 or higher from AdoptOpenJDK.
	•	Add Java to your system PATH.
Verify installation:

java -version

Setup Steps

1. Set JAVA_HOME Environment Variable
	•	Locate your Java installation directory (e.g., C:\Program Files\Java\jdk-xx).
	•	Set the JAVA_HOME variable:

[System.Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Path\To\Java", "User")


	•	Add %JAVA_HOME%\bin to your system PATH.

Verify:

echo %JAVA_HOME%

2. Download SSL Certificates
	•	Use the export_nexus_certificate.py script to download certificates from your Nexus repository:

python export_nexus_certificate.py https://nexus.example.com --output nexus_cert.crt


	•	Place the downloaded certificates in a known directory (e.g., C:\path\to\certs).

3. Setup pip.ini for Nexus
	•	Create the pip.ini configuration file:

[global]
index-url = https://nexus.example.com/repository/pypi-all
trusted-host = nexus.example.com

[http-basic]
nexus.example.com.username = <your-username>
nexus.example.com.password = <your-password>


	•	Save it at:
	•	Windows: %APPDATA%\pip\pip.ini
	•	Linux/Mac: ~/.config/pip/pip.conf.

4. Install and Setup Poetry with pipx
	•	Install pipx:

python -m pip install --user pipx
python -m pipx ensurepath


	•	Install Poetry:

pipx install poetry



Verify Poetry installation:

poetry --version

5. Setup Poetry Nexus Environment Variables
	•	Set environment variables for Nexus authentication:

[System.Environment]::SetEnvironmentVariable("POETRY_HTTP_BASIC_NEXUS_USERNAME", "<your-username>", "User")
[System.Environment]::SetEnvironmentVariable("POETRY_HTTP_BASIC_NEXUS_PASSWORD", "<your-password>", "User")
[System.Environment]::SetEnvironmentVariable("POETRY_CERTIFICATE_NEXUS_CERT", "C:\path\to\certs\nexus_cert.crt", "User")



Restart your shell to apply the changes.

6. Setup Poetry Temporary Directory
	•	Create a dedicated directory for Poetry’s temporary files:

mkdir C:\poetrytemp
[System.Environment]::SetEnvironmentVariable("TMPDIR", "C:\poetrytemp", "User")

7. Setup Hadoop WinUtils
	•	Download winutils.exe compatible with your Hadoop version.
	•	Place it in a directory like C:\hadoop\bin.
	•	Set the environment variable:

[System.Environment]::SetEnvironmentVariable("HADOOP_HOME", "C:\hadoop", "User")



Add %HADOOP_HOME%\bin to your system PATH.

8. Setup PyCharm
	•	Download and install PyCharm from JetBrains.
	•	Configure PyCharm:
	1.	Interpreter:
	•	Add the Python interpreter used for this setup.
	•	Go to File -> Settings -> Project -> Python Interpreter.
	2.	Poetry:
	•	Add Poetry as the project’s dependency manager.
	•	Enable virtual environments.
	3.	Environment Variables:
	•	Add POETRY_HTTP_BASIC_NEXUS_USERNAME, POETRY_HTTP_BASIC_NEXUS_PASSWORD, and POETRY_CERTIFICATE_NEXUS_CERT in Run/Debug Configurations.

Verification
	1.	Test Python and Java installations:

python --version
java -version


	2.	Verify Poetry:

poetry --version


	3.	Test Nexus configuration:

pip install <package-name>


	4.	Run a sample Python project in PyCharm to confirm the setup.

Troubleshooting
	•	Certificates not working:
	•	Ensure the correct certificates are downloaded and paths are configured.
	•	Environment variables not recognized:
	•	Restart your shell or system to apply changes.
	•	Poetry fails to connect to Nexus:
	•	Verify the poetry config and environment variable settings:

poetry config --list

Let me know if you need more refinements! 🚀
