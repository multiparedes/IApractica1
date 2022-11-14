import sys
sys.path.append('C:\\Users\\Silvia\\Documents\\Escola\\3rCarrera\\IA\\ia')

from practica1 import agent, joc, agent_amplada


def main():
    rana = agent_amplada.Rana("Miquel")
    lab = joc.Laberint([rana], parets=True)
    lab.comencar()


if __name__ == "__main__":
    main()
