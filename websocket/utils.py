from channels import Group


def get_dest(dest):
    return Group("mirror") if dest is None else dest
