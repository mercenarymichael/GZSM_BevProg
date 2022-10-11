
class Team:
    def __init__(self, name, project, role):
        self._name = name
        self._project = project
        self._role = role
        print("-- Developer létrehozva. --")
    #

    def __str__(self):
        return f"{self._name} a {self._project}-en " \
               f"dolgozik {self._role} szerepkörben."
    #

    def __eq__(self, coworker):
        if isinstance(coworker, Team):
            if self._name == coworker._name and self._role == coworker._role and self._project == coworker._project:
                print("Duplikalt bejegyzes!")
            elif self._project == coworker._project:
                return self._project == coworker._project


def egyenloseg(devs):
    for i in range(0, len(devs)):
        for j in range(i+1, len(devs)):
            if devs[i] == devs[j]:
                print(f"{devs[i]._name} és {devs[j]._name} "
                      f"dolgoznak egy projekten")


def main():
    dev1 = Team("Ricsi", "SolArch", "Frontend")
    print(dev1)
    dev2 = Team("Angéla", "ZerTeng", "Tesztelő")
    print(dev2)
    dev3 = Team("Peti", "KefERP", "Backend")
    print(dev3)
    dev4 = Team("Éva", "KefERP", "Frontend")
    print(dev4)
    dev5 = Team("Éva", "KefERP", "Frontend")
    print(dev5)

    devs = [dev1, dev2, dev3, dev4, dev5]
    egyenloseg(devs)

if __name__ == "__main__":
    main()