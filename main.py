from pyswip import Prolog
from argparse import ArgumentParser
from gooey import Gooey
swipl = Prolog()
swipl.consult("test1.pl")

MOODS = [ans["M"] for ans in swipl.query("mood(M)")]
PTYPE = [ans["P"] for ans in swipl.query("personality(P)")]

def selector(mood, ptype):
    return list(swipl.query(f"song(S,_,{mood},{ptype})."))

@Gooey
def main():
    parser = ArgumentParser(description="Input personality type and mood for music suggestion")
    parser.add_argument("-m", "--mood", choices=MOODS, required=True)
    parser.add_argument("-p", "--personality", choices=PTYPE, required=True)
    args = parser.parse_args()
    print(selector(args.mood, args.personality))


if __name__ == "__main__":
    main()
