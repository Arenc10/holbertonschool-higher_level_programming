#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    prefix = "__"
    string = '\n'.join([str(item) for item in dir(hidden_4) if not item.startswith(prefix)])
    print(f"{string}")
