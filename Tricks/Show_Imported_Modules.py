import pip
for i in pip.get_installed_distributions(local_only=True):
    print(i)

