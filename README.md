Install Dependencies:

First, ensure you have all the necessary dependencies installed by running:
bash
Copy
pip install -r requirements.txt
This will install the required packages, including any user-defined packages, and set up your environment.
Avoid Rebuilding User-Defined Packages:

If you need to update any libraries or add new ones to requirements.txt, follow these steps to avoid rebuilding user-defined packages every time:
Temporarily comment out the line -e . in the requirements.txt file.
Then, run:
pip install -r requirements.txt
This ensures that only the external libraries are updated, and the user-defined package is not rebuilt.
Rebuild User-Defined Packages (If Necessary):

If you make changes to any user-defined package and need to rebuild it, uncomment the -e . line in requirements.txt and run the installation again:
pip install -r requirements.txt
