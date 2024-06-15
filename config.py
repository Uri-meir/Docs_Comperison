import yaml


def load_config(conf_path):
    with open(conf_path, 'r') as file:
        config = yaml.safe_load(file)
        print(f"Configuration loaded successfully from {conf_path}")
        return config

