define player_name = "Blanche"
define chap2_stars = [('star_pisces', _('Pisces')), ('star_leo', _('Leo')), ('star_volans', _('Volans')), ('star_piscis_austrinus', _('Piscis austrinus'))]
define encore = ""
define good = 0
define neutral = 0
define bad = 0

default tutorial_boot_found = False

define lake_phishing_talked_axolotl = 0
define lake_phishing_fished_axolotl = False
define lake_phishing_fished_boot = False
define lake_phishing_fished_fish1 = False
define lake_phishing_fished_fish2 = False

default image_cutter_time_factor = 1.

transform crystal_position:
    xalign 0.5
    yalign 0.5

default persistent.reached_end_good = False
default persistent.reached_end_neutral = False
default persistent.reached_end_bad = False
default persistent.last_reached_end = None
