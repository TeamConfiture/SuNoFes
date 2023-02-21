init python in achievement:
    register(_("achievement_chap1_minigame_done"))
    register(_("achievement_chap2_minigame_done"))
    register(_("achievement_chap3_minigame_done"))
    register(_("achievement_chap4_minigame_done"))
    register(_("achievement_chap5_minigame_done"))
    register(_("achievement_chap6_minigame_done"))
    register(_("achievement_chap7_minigame_done"))

    register(_("achievement_ending_good"))
    register(_("achievement_ending_neutral"))
    register(_("achievement_ending_bad"))
    register(_("achievement_ending_all"))

    register(_("achievement_new_friend"))
    register(_("achievement_walk"))
    register(_("achievement_later"))

    class NotifyBackend(Backend):
        def grant(self, name):
            if not has(name):
                renpy.notify(__("Nouveau succès : {}").format(__(name)))

    # Add as first to be able to check before PersistentBackend updates values
    backends.insert(0, NotifyBackend())
