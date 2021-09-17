import winreg


class RegistryPaths:
    """Class to get all the paths of the registry keys.

    Args:
        hkey (Const): any one of the predefined HKEY_* constants]
            {HKEY_CLASSES_ROOT,
            HKEY_CURRENT_USER,
            HKEY_LOCAL_MACHINE,
            HKEY_USERS,
            HKEY_CURRENT_CONFIG}

        sub_key (str): the subkey to open
        value_name (str): the value to retrieve
    """

    def __init__(self, hkey=-1, sub_key=-1, value_name=-1):
        self.HKEY_constants = hkey
        self.sub_key = sub_key
        self.value_name = value_name

    def get_value_name(self):
        return self.value_name

    def set_value_name(self, value):
        self.value_name = value

    def __str__(self):
        return f'{self.value_name}'

    def get_root_key(self, hkey):
        """Return the root key for the given root key name.

        Args:
            hkey (str): the name of the root key

        Returns:
            Const: the root key with winreg module
        """
        # Get the root key
        if root_key == "HKEY_CLASSES_ROOT":
            return winreg.HKEY_CLASSES_ROOT
        elif root_key == "HKEY_CURRENT_USER":
            return winreg.HKEY_CURRENT_USER
        elif root_key == "HKEY_LOCAL_MACHINE":
            return winreg.HKEY_LOCAL_MACHINE
        elif root_key == "HKEY_USERS":
            return winreg.HKEY_USERS
        elif root_key == "HKEY_CURRENT_CONFIG":
            return winreg.HKEY_CURRENT_CONFIG
        else:
            raise ValueError("Invalid root key: " + root_key)

    @staticmethod
    def get_registry_value(sub_key
                           , value_name):
        """Get a value from the Windows registry by passing the root key,
        subkey, and value name.

        Args:
            HKEY_constants (Const): any one of the predefined HKEY_* constants]
                {HKEY_CLASSES_ROOT,
                HKEY_CURRENT_USER,
                HKEY_LOCAL_MACHINE,
                HKEY_USERS,
                HKEY_CURRENT_CONFIG}

            sub_key (str): the subkey to open
            value_name (str): the value to retrieve

        Returns:
            str: the value from the registry
        """
        # Open the registry key
        try:
            root_key = get_root_key(HKEY_constants)
            # Open the registry key
            registry_key = winreg.OpenKey(root_key, sub_key)
            # Get the value
            value, value_type = winreg.QueryValueEx(registry_key, value_name)
            # Close the registry key
            winreg.CloseKey(registry_key)
            return value
        except FileNotFoundError:
            return "Not found"


keypath = r"Software\Mikero\ArmA3"

mik_tool_path = get_registry_value("HKEY_CURRENT_USER", keypath, "path")

print(mik_tool_path)

# get mikero tools path
# key = HKEY_CURRENT_USER\Software\Mikero\ArmA3p
# ValueName = path
#  returns mikero tools path ie C:\Program Files (x86)\Mikero\DePboTools

# get arma3p (pdrive builder) path
# key = HKEY_CURRENT_USER\Software\Mikero\ArmA3p
# valuename = exe
# returns path and.cmd name ie C:\Program Files (x86)\Mikero\DePboTools\bin\ArmA3p.cmd

# get arma3 Addon Builder Path
# key = =HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\bohemia interactive\AddonBuilder
# valuename = path
# returns path ie D:\Games\Steam\steamapps\common\Arma 3 Tools\AddonBuilder


# get Arma3 path
# key = HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\bohemia interactive\ArmA3
# valuename = main
# returns path ie C:\SteamLibrary\steamapps\common\Arma 3
