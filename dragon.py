from creature import Creature


class Dragon(Creature):
    def __init__(self, name, health, attack):
        Creature.__init__(self, name, health, attack)


    ascii_alive = """
                                    
                                                                 __----~~~~~~~~~~~------___
                                                      .  .   ~~//====......          __--~ ~~
                                      -.            \_|//     |||\_\  ~~~~~~::::... /~
                                   ___-==_       _-~o~  \/    |||  \_\            _/~~-
                           __---~~~.==~||\=_    -_--~/_-~|-   |\_\   \_\        _/~
                       _-~~     .=~    |  \_\-_    '-~7  /-   /  ||    \      /
                     .~       .~       |   \_\ -_    /  /-   /   ||      \   /
                    /  ____  /         |     \_\ ~-_/  /|- _/   .||       \ /
                    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\_
                             '         ~-|      /|    |-~\~~       __--~~
                                         |-~~-_/ |    |   ~\_   _-~            /\_
                                              /  \     \__   \/~                \__
                                          _--~ _/ | .-~~____--~-/                  ~~==.
                                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                                    -_     ~\      ~~---l__i__i__i--~~_/
                                                    _-~-__   ~)  \--______________--~~
                                                  //.-~~~-~_--~- |-------~~~~~~~~
                                                         //.-~~~--\_
                                                         
    """

    ascii_dead = """
                                    
                                                                 __----~~~~~~~~~~~------___
                                                      .  .   ~~//====......          __--~ ~~
                                      -.            \_|//     |||\_\  ~~~~~~::::... /~
                                   ___-==_       _-~X~  \/    |||  \_\            _/~~-
                           __---~~~.==~||\=_    -_--~/_-~|-   |\_\   \_\        _/~
                       _-~~     .=~    |  \_\-_    '-~7  /-   /  ||    \      /
                     .~       .~       |   \_\ -_    /  /-   /   ||      \   /
                    /  ____  /         |     \_\ ~-_/  /|- _/   .||       \ /
                    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\_
                             '         ~-|      /|    |-~\~~       __--~~
                                         |-~~-_/ |    |   ~\_   _-~            /\_
                                              /  \     \__   \/~                \__
                                          _--~ _/ | .-~~____--~-/                  ~~==.
                                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                                    -_     ~\      ~~---l__i__i__i--~~_/
                                                    _-~-__   ~)  \--______________--~~
                                                  //.-~~~-~_--~- |-------~~~~~~~~
                                                         //.-~~~--\_
            
"""