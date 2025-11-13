# SSH - Setting up Access and Acessing it on Instances
Everything related to our use of SSH should go here.

## Setting up SSH Access
Vist https://docs.mdoq.io/hc/en-gb/articles/4409892812561-Generating-SSH-Key-Pair-Using-MobaXterm for how to generate SSH keys.

1. Go the production instance of the client you want to access via SSH.
2. Click "Settings".
3. Open the "SSH" tab.
4. Click the blue plus to add your identity.
5. Enter a name in the "name" field.
6. Enter your public SSH key in the "Public Key" field.
7. Click the "Save" box that appears at the bottom of the box.

## Getting SSH on Instances
To have your newly created SSH access usable on instances you'll have to go the instance you want access on and follow the below steps.

1. Click "Sync".
2. Click "SELECT COMPONENTS TO SYNCHORONIZE".
3. Select "SSH" and then click "SYNCHORONIZE".
4. Once the instance has completed the resync, you'll be able to use SSH on that instance.

## Entering SSH Termial
Here's how to get into the SSH termial on Mdoq isntances.

1. Go to the instance you want to access the the SSH termial on.
2. Click "Support".
3. Click the "open in new tab" icon to the right of "Web SSH".
4. Click "Choose file" and choose your private SSH key.
5. Enter your passcode into the "Passphrase" field.
6. Click "Connect".
7. Your now in the SSH termial for the instance.
