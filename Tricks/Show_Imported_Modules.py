import pip

modules = set([])
for module in pip.get_installed_distributions(local_only=True):
    print(module)
    modules.add(module)

modules = list(modules)
