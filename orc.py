from creature import Creature


class Orc(Creature):
    def __init__(self, name, health, attack, inventory):
        Creature.__init__(self, name, health, attack, inventory)


    ascii_alive = """
                                                      (    )
                                                      ((((()))
                                                      |O\ /O)|
                                                      ( (  _')
                                                       (._.  /\__
                                                      ,\___,/ '  ')
                                        '.,_,,       (  .- .   .    )
                                         \   \\     ( '        )(    )
                                          \   \\    \.  _.__ ____( .  |
                                           \  /\\   .(   .'  /\  '.  )
                                            \(  \\.-' ( /    \/    \)
                                             '  ()) _'.-|/\/\/\/\/\|
                                                 '\\ .( |\/\/\/\/\/|
                                                   '((  \    /\    /
                                                   ((((  '.__\/__.')
                                                    ((,) /   ((()   )
                                                     "..-,  (()("   /
                                                      _//.   ((() ."
                                              _____ //,/" ___ ((( ', ___
                                                               ((  )
                                                                / /
                                                              _/,/'
                                                            /,/,"
    """

    ascii_dead = """
                                                      (    )
                                                      ((((()))
                                                      |X\ /X)|
                                                      ( (  _')
                                                       (._.  /\__
                                                      ,\___,/ '  ')
                                        '.,_,,       (  .- .   .    )
                                         \   \\     ( '        )(    )
                                          \   \\    \.  _.__ ____( .  |
                                           \  /\\   .(   .'  /\  '.  )
                                            \(  \\.-' ( /    \/    \)
                                             '  ()) _'.-|/\/\/\/\/\|
                                                 '\\ .( |\/\/\/\/\/|
                                                   '((  \    /\    /
                                                   ((((  '.__\/__.')
                                                    ((,) /   ((()   )
                                                     "..-,  (()("   /
                                                      _//.   ((() ."
                                              _____ //,/" ___ ((( ', ___
                                                               ((  )
                                                                / /
                                                              _/,/'
                                                            /,/,"
"""