
---

## Godfall

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_NO_TARGET/|/DOTA_ABILITY_BEHAVIOR_CHANNELLED** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET**.
* Cast point increased from **0** to **0.6**.
* Cooldown increased from **70** to **140**.
* Var type changed from **FIELD_INTEGER** to **FIELD_FLOAT**.
* Duration increased from **7** to **8.0**.

---

## Lightburst


---

## Raise the Shield

* Script file changed from **lua/abilities/alexander_radiant** to **lua/abilities/alexander_raise_the_shield**.
* Behavior changed from **DOTA_ABILITY_BEHAVIOR_NO_TARGET/|/DOTA_ABILITY_BEHAVIOR_IGNORE_PSEUDO_QUEUE/|/DOTA_ABILITY_BEHAVIOR_IMMEDIATE** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET**.
* Texture name changed from **alexander_radiant** to **alexander_raise_the_shield**.
* Cast range increased from **325** to **375**.
* Cast point increased from **0** to **0.45**.
* Mana cost increased from **80** to **170**.
* Duration rescaled from **8** to **8.0**.
* Radius increased from **400** to **450**.

---

## Black Insignia

* Hits increased from **5** to **6**.

---

## Compression Sphere

* Cast range increased from **400** to **750**.
* Cooldown reduced from **23** to **14**.

---

## Spatial Rift

* Animation playback rate increased from **0.95** to **1.15**.
* Channel time increased from **0.75** to **2.00/1.50/1.00/0.50**.
* Cast range reduced from **800/1000/1200/1400** to **1200**.
* Cooldown reduced from **17/16/15/14** to **9**.
* Mana cost reduced from **125** to **75**.
* Damage reduced from **50/125/200/275** to **100/125/150/175**.

---

## Desolation

* Cast range increased from **550** to **600**.
* Cast point increased from **0.4** to **0.5**.
* Cooldown increased from **16** to **25/22/19/16**.
* Mana cost reduced from **115/120/125/130** to **145**.
* Damage reduced from **60/80/100/120** to **125**.
* Dps increased from **10/20/30/40** to **15/25/35/45**.
* Var type changed from **FIELD_INTEGER** to **FIELD_INTEGER**.
* Duration increased from **6** to **8.0**.
* Radius increased from **400** to **550**.

---

## Fulmination

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_PASSIVE** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET**.
* Cast animation changed from **ACT_DOTA_CAST_ABILITY_2** to **ACT_DOTA_CAST_ABILITY_4**.
* Cast point rescaled from **0** to **0.0**.
* Cooldown increased from **0** to **40/32/24/16**.
* Mana cost increased from **0** to **110**.
* Var type changed from **FIELD_FLOAT** to **FIELD_FLOAT**.
* Soundfile changed from **soundevents/game_sounds_heroes/game_sounds_oracle.vsndevts** to **soundevents/hero_bahamut.vsndevts**.

---

## Mega Flare

* Base class changed from **ability_datadriven** to **ability_lua**.
* Damage type changed from **DAMAGE_TYPE_PURE** to **DAMAGE_TYPE_MAGICAL**.
* Spell immunity type changed from **SPELL_IMMUNITY_ENEMIES_YES** to **SPELL_IMMUNITY_ENEMIES_NO**.
* Ao eradius increased from **400** to **700**.
* Cast range reduced from **1500** to **975**.
* Cast point reduced from **0.4** to **0.3**.
* Cooldown increased from **110** to **110/100/90**.
* Mana cost increased from **230** to **350/400/450**.
* Damage inner increased from **225/300/375** to **300/400/500**.
* Radius inner reduced from **325** to **275**.
* Damage outer increased from **175/225/275** to **200/250/300**.
* Speed changed from **%speed** to **%speed**.
* Script file changed from **heroes/bahamut_abilities.lua** to **heroes/bahamut_abilities.lua**.
* Function changed from **MegaFlare** to **MegaFlare**.
* Damage changed from **%damage_inner** to **%damage_inner**.
* Damage2 changed from **%damage_outer** to **%damage_outer**.
* Radius changed from **%radius_inner** to **%radius_inner**.
* Radius2 changed from **%radius_outer** to **%radius_outer**.
* Passive rescaled from **0** to **0**.
* Is hidden rescaled from **0** to **0**.
* Is debuff rescaled from **1** to **1**.
* Effect name changed from **particles/units/heroes/hero_bahamut/desolation_model_secondary.vpcf** to **particles/units/heroes/hero_bahamut/desolation_model_secondary.vpcf**.
* Effect attach type changed from **attach_hitloc** to **attach_hitloc**.
* Aura changed from **modifier_desolation_aura** to **modifier_desolation_aura**.
* Aura  radius rescaled from **400** to **400**.
* Aura  teams changed from **DOTA_UNIT_TARGET_TEAM_FRIENDLY** to **DOTA_UNIT_TARGET_TEAM_FRIENDLY**.
* Aura  types changed from **DOTA_UNIT_TARGET_HERO/|/DOTA_UNIT_TARGET_BASIC** to **DOTA_UNIT_TARGET_HERO/|/DOTA_UNIT_TARGET_BASIC**.
* Aura  flags changed from **DOTA_UNIT_TARGET_FLAG_NONE** to **DOTA_UNIT_TARGET_FLAG_NONE**.
* Aura  apply to caster rescaled from **1** to **1**.
* Think interval rescaled from **1.0** to **1.0**.
* Target changed from **TARGET** to **TARGET**.
* Type changed from **DAMAGE_TYPE_MAGICAL** to **DAMAGE_TYPE_MAGICAL**.
* Damage changed from **%dps** to **%dps**.

---

## Reckoning

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_UNIT_TARGET/|/DOTA_ABILITY_BEHAVIOR_AURA** to **DOTA_ABILITY_BEHAVIOR_UNIT_TARGET**.
* Cast range reduced from **800** to **600**.
* Cast point reduced from **0.3** to **0.2**.
* Cooldown reduced from **45** to **20**.
* Mana cost increased from **0** to **95**.
* Var type changed from **FIELD_INTEGER** to **FIELD_FLOAT**.
* Duration increased from **6** to **3.5/4.0/4.5/5.0**.
* Particle changed from **particles/units/heroes/hero_bahamut/desolation_cast.vpcf** to **particles/units/heroes/hero_bahamut/reckoning_drain_buff.vpcf**.

---

## Emerald Fang

* Animation playback rate rescaled from **0.0** to **0.0**.

---

## Firebolt

* Cast range increased from **575** to **675**.
* Cooldown reduced from **14.00/13.00/12.00/11.00** to **7.00**.

---

## Deathtouch

* Animation playback rate reduced from **1.5** to **1.0**.
* Cast range increased from **150** to **175**.
* Cast point increased from **0.1** to **0.5**.
* Dot amount increased from **50/80/110** to **80/160/240**.

---

## To Dust

* Cooldown increased from **45** to **40/35/30/25**.
* Radius increased from **500** to **700**.

---

## Displace

* Cooldown reduced from **32/28/24/20** to **32/26/20/14**.

---

## Realign

* Animation playback rate increased from **0.50** to **0.75**.
* Cast range reduced from **500** to **425**.
* Cast point reduced from **0.6/0.6/0.6/0.6** to **0.4/0.4/0.4/0.4**.
* Cooldown reduced from **7** to **6**.
* Mana cost increased from **90** to **120**.
* Shock radius reduced from **500** to **425**.
* Damage increased from **90/120/150/180** to **75/150/225/300**.
* Linked special bonus changed from **special_bonus_fate_3** to **special_bonus_fate_4**.

---

## faust_netherglyph

* Cast range reduced from **275** to **225**.
* Cooldown increased from **60** to **75**.
* Mana cost reduced from **100** to **0**.
* Spell a mp increased from **15** to **30**.
* Mana regen increased from **6/8/10** to **25**.
* Duration reduced from **10.0/12.0/14.0** to **8.0**.
* Radius reduced from **275** to **225**.

---

## Berserk

* Cooldown reduced from **80/60/40** to **60**.
* Mana cost increased from **0** to **50**.
* Bonus attackspeed increased from **150/200/250** to **200/300/400**.
* Duration reduced from **6.0** to **2.5**.

---

## Rend

* Reset time rescaled from **6** to **6**.

---

## Roar

* Cooldown increased from **12** to **10/8/6/4**.
* Damage reduced from **75/125/175/225** to **50/100/150/200**.
* Bonus movespeed reduced from **1/2/3/4** to **3**.
* Bonus attackspeed reduced from **5/10/15/20** to **10**.
* Bonus damage reduced from **4/6/8/10** to **5**.

---

## Clearance Sale

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_NO_TARGET** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET/|/DOTA_ABILITY_BEHAVIOR_IMMEDIATE**.
* Damage increased from **100/150/200** to **275/390/505**.
* Radius increased from **300** to **350**.
* Duration reduced from **10** to **8**.
* Slow reduced from **-20** to **-50/-75/-100**.
* Interval increased from **0.4** to **1.00**.

---

## Kamikaze

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_NO_TARGET** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET/|/DOTA_ABILITY_BEHAVIOR_IMMEDIATE**.
* Cooldown reduced from **60/50/40/30** to **20**.
* Damage increased from **150/200/250/300** to **250/300/350/400**.
* Movespeed bonus reduced from **15/20/25/30** to **40**.
* Health damage reduced from **50** to **35**.
* Total reduced from **50** to **0**.
* Stun reduced from **1.4** to **0.7**.

---

## Rocket Blast

* Cast range reduced from **1600** to **1100**.
* Cast point reduced from **0.40** to **0.25**.
* Cooldown reduced from **8.0/7.5/7.0/6.5** to **9.5**.
* Damage reduced from **125/200/275/350** to **100/175/250/325**.
* Mana cost reduced from **60/75/90/105** to **95**.
* Range reduced from **1600** to **1100**.
* Speed reduced from **1200** to **1000**.
* Var type changed from **FIELD_FLOAT** to **FIELD_INTEGER**.
* Radius reduced from **300** to **225**.
* Projectile speed rescaled from **1000** to **1000**.

---

## Whoops


---

## Rapidfire

* Damage reduction increased from **-80/-72/-64/-56** to **-70/-55/-40/-25**.

---

## Freedom Strike!

* Cooldown reduced from **12/10/8/6** to **5**.
* Mana cost reduced from **60** to **55**.
* Radius increased from **250** to **275**.
* Slow increased from **-10/-12/-14/-16** to **-25**.
* Duration increased from **3** to **2.0/2.5/3.0/3.5**.

---

## Heroic Soul

* Cooldown reduced from **20/18/16/14** to **14**.
* Bonus movespeed reduced from **40** to **32**.
* Damage reduction duration increased from **0.5** to **0.75**.

---

## Justice Kick!

* Cast point reduced from **0.3** to **0.25**.
* Cooldown reduced from **8/7/6/5** to **5**.
* Mana cost increased from **50** to **55**.
* Duration increased from **1** to **1.3**.

---

## Boltblast

* Cast range reduced from **975** to **600**.
* Cast point reduced from **0.4** to **0.2**.
* Cooldown reduced from **8** to **5**.
* Explosion damage reduced from **120/180/240/300** to **100/140/180/220**.

---

## Lightning Daggers

* Cast range increased from **675** to **400/450/500/550**.
* Cooldown increased from **3.5** to **5**.
* Mana cost reduced from **35/40/45/50** to **70**.
* Damage increased from **50/60/70/80** to **60/80/100/120**.
* Duration reduced from **0.75** to **0.25**.
* Bounces reduced from **3/4/5/6** to **5**.

---

## Overload

* Type changed from **DOTA_ABILITY_TYPE_BASIC** to **DOTA_ABILITY_TYPE_ULTIMATE**.
* Cast range increased from **250** to **375**.
* Cast point increased from **0** to **0.3**.
* Cooldown increased from **2.00** to **10/9/8**.
* Mana cost reduced from **40/50/60/70** to **100**.
* Damage increased from **50/80/110/140** to **150/200/250**.
* Radius increased from **250** to **375**.
* Var type changed from **FIELD_INTEGER** to **FIELD_FLOAT**.
* Soundfile changed from **soundevents/game_sounds_heroes/game_sounds_stormspirit.vsndevts** to **soundevents/hero_lightning.vsndevts**.
* Particle changed from **particles/units/heroes/hero_stormspirit/stormspirit_overload_discharge.vpcf** to **particles/units/heroes/hero_lightning/overload.vpcf**.

---

## Spark

* Type changed from **DOTA_ABILITY_TYPE_ULTIMATE** to **DOTA_ABILITY_TYPE_BASIC**.
* Cast range reduced from **900** to **300**.
* Radius reduced from **900** to **300**.
* Slow reduced from **-5/-10/-15** to **-10/-15/-20/-25**.
* Particle changed from **particles/units/heroes/hero_lightning/spark.vpcf** to **particles/units/heroes/hero_lightning/spark_unit_damage.vpcf**.
* Soundfile changed from **soundevents/game_sounds_heroes/game_sounds_zuus.vsndevts** to **soundevents/hero_lightning.vsndevts**.

---

## Beneath The Mask

* Cooldown increased from **10** to **13/12/11/10**.
* Slow increased from **8/12/16/20** to **16/24/32/40**.
* Attack speed steal increased from **30/40/50/60** to **40/60/80/100**.
* Duration reduced from **2/3/4/5** to **4.5**.

---

## Finisher

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_UNIT_TARGET** to **DOTA_ABILITY_BEHAVIOR_UNIT_TARGET/|/DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_MOVEMENT**.
* Cast range reduced from **750** to **600**.
* Cast point increased from **0.1** to **0.48**.
* Cooldown reduced from **9/8/7/6** to **15**.
* Mana cost increased from **75** to **95**.
* Var type changed from **FIELD_INTEGER** to **FIELD_INTEGER**.
* Slow rescaled from **140** to **140**.
* Slow duration increased from **0.75** to **0.80**.
* Stun reduced from **0.50/0.75/1.00/1.25** to **0.70**.

---

## Flashbang

* Cast range increased from **350** to **375**.
* Cast point increased from **0.2** to **0.3**.
* Cooldown reduced from **16/14/12/10** to **12**.
* Damage increased from **100** to **125**.
* Duration increased from **1.50/2.25/3.00/3.75** to **2.00/2.75/3.50/4.25**.
* Radius increased from **350** to **375**.

---

## Calling Card

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_POINT** to **DOTA_ABILITY_BEHAVIOR_POINT/|/DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_MOVEMENT**.
* Damage type changed from **DAMAGE_TYPE_MAGICAL** to **DAMAGE_TYPE_PHYSICAL**.
* Cast range increased from **775** to **1250**.
* Cast point increased from **0.1** to **0.22**.
* Cooldown increased from **15** to **40/35/30**.
* Mana cost increased from **50** to **125**.
* Var type changed from **FIELD_INTEGER** to **FIELD_INTEGER**.
* Duration increased from **5** to **6**.
* Radius reduced from **900** to **250**.

---

## Flux Field

* Cast point reduced from **0.5** to **0.1**.
* Damage per cast increased from **30/60/90/120** to **80/160/240/320**.

---

## Gravity Pulse

* Animation play back rate increased from **0.80** to **1.3**.
* Cast range reduced from **525** to **475**.
* Cast point reduced from **0.6** to **0.2**.
* Cooldown reduced from **10** to **8**.

---

## Micronebula

* Cast point reduced from **0.3** to **0.1**.
* Mana cost increased from **75** to **95**.

---

## Warpstar

* Cast range increased from **1400** to **1000/1400/1800**.
* Damage increased from **125/200/275** to **200/275/350**.

---

## Shadowstep

* Cooldown increased from **60** to **40/35/30/25**.
* Duration increased from **6.0** to **5.0/6.0/7.0/8.0**.
* Delay reduced from **4.00/3.25/2.50/1.75** to **4.00**.
* Bonus movespeed increased from **30** to **12/20/28/36**.

---

## pride_elyats_bellow


---

## pride_lionheart


---

## pride_merciless


---

## Amplify

* Cast point reduced from **0.3** to **0.15**.
* Damage increased from **10/20/30/40** to **30/50/70/90**.
* Duration reduced from **5** to **2.5**.
* Radius reduced from **400** to **350**.
* Targets increased from **1/2/3/4** to **2/3/4/5**.
* Slow duration increased from **1.65** to **2.25**.

---

## Arc Twister

* Cooldown reduced from **9/8/7/6** to **5**.
* Mana cost increased from **75** to **115**.
* Delay increased from **0.15** to **0.16**.

---

## Static Blade

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_NO_TARGET/|/DOTA_ABILITY_BEHAVIOR_TOGGLE** to **DOTA_ABILITY_BEHAVIOR_PASSIVE**.
* Cooldown reduced from **4** to **2.5**.

---

## Thunder Roar

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_NO_TARGET** to **DOTA_ABILITY_BEHAVIOR_POINT/|/DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES**.
* Cast animation changed from **ACT_DOTA_CAST_ABILITY_2** to **ACT_DOTA_CAST_ABILITY_1**.
* Cast range increased from **475** to **1100/1200/1300**.
* Cast point increased from **0.3** to **0.6**.
* Cooldown reduced from **80/75/70** to **60/55/50**.
* Mana cost increased from **200** to **225/250/275**.
* Damage increased from **100/125/150** to **250/325/400**.
* Bolt radius reduced from **300** to **275**.

---

## Scarab Curse

* Base damage increased from **10/15/20/25** to **15/20/25/30**.
* Percent damage reduction increased from **15** to **12/20/28/36**.

---

## Dark Hunger

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_PASSIVE** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET**.
* Cast range increased from **0** to **325**.
* Cast point increased from **0** to **0.2**.
* Cooldown increased from **0** to **19**.
* Mana cost increased from **0** to **110**.

---

## Shadowshift


---

## Stalk

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_UNIT_TARGET** to **DOTA_ABILITY_BEHAVIOR_UNIT_TARGET/|/DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_MOVEMENT/|/DOTA_ABILITY_BEHAVIOR_DONT_ALERT_TARGET/|/DOTA_ABILITY_BEHAVIOR_IGNORE_BACKSWING**.
* Target flags changed from **DOTA_UNIT_TARGET_FLAG_MAGIC_IMMUNE_ENEMIES/|/DOTA_UNIT_TARGET_FLAG_NOT_ANCIENTS** to **DOTA_UNIT_TARGET_FLAG_MAGIC_IMMUNE_ENEMIES**.
* Damage type changed from **DAMAGE_TYPE_PURE** to **DAMAGE_TYPE_PHYSICAL**.
* Cast range increased from **900** to **1100**.
* Cooldown reduced from **24/18/12/6** to **12**.
* Mana cost increased from **110** to **75/85/95/105**.
* Proc damage reduced from **50/100/150/200** to **40/80/120/160**.
* Movespeed bonus increased from **15/20/25/30** to **12/20/28/36**.
* Slow reduced from **15/20/25/30** to **12**.
* Duration increased from **4.5** to **6.0**.

---

## Venomous

* Damage increased from **5/10/15/20** to **8/14/20/26**.
* Var type changed from **FIELD_INTEGER** to **FIELD_FLOAT**.
* Duration reduced from **6** to **4.0**.

---

## Cryst Whorl

* Damage increased from **60/120/180/240** to **100/175/250/325**.
* Slow increased from **20/25/30/35** to **15/30/45/60**.
* Initial damage increased from **60** to **100**.

---

## Glacial Impact

* Cast point increased from **0.1** to **0.4**.
* Cooldown reduced from **75** to **70**.
* Stun duration increased from **0.8/1.0/1.2** to **1.4/2.0/2.6**.
* Damage reduced from **275/400/525** to **200/300/400**.
* Radius reduced from **275/300/325** to **400**.

---

## Icicle Barrage

* Cooldown increased from **10** to **16**.
* Icicles increased from **15/20/25/30** to **10/20/30/40**.
* Damage increased from **20** to **25**.
* Range reduced from **1400** to **1200**.

---

## Doomflame Free Pathing

* Value reduced from **500** to **0**.

---

## +350 Ward of the Emerald Flame Range

* Value reduced from **600** to **350**.

---

## -8s Firebolt Cooldown

* Value reduced from **12** to **8**.

---

## +60 Realign Damage/Heal

* 01 changed from **fate_realign** to **fate_ancestral_visions**.
* Var type changed from **FIELD_INTEGER** to **FIELD_FLOAT**.
* Value reduced from **60** to **0.5**.

---

## +20% Ancestral Recall Restore

* 01 changed from **fate_ancestral_recall** to **fate_realign**.
* Value increased from **20** to **175**.

---

## +2% Rend Damage Amp

* Value reduced from **10** to **2**.

---

## Roar 1s Stun

* Value increased from **0** to **1**.

---

## 

* 01 changed from **fury_berserk** to **fury_bloodsport**.
* Var type changed from **FIELD_INTEGER** to **FIELD_FLOAT**.
* Value reduced from **4** to **0.3**.

---

## Megaton Blast

* Cast range reduced from **900** to **750**.
* Cooldown increased from **25/21/17/13** to **30/23/16/9**.
* Stun reduced from **0.75** to **0.50**.

---

## Mosquito Missiles

* Channel time reduced from **1.5** to **0.8**.
* Cooldown reduced from **16/14/12/10** to **8**.
* Interval reduced from **0.20/0.15/0.10/0.05** to **0.05**.
* Damage increased from **20** to **10/20/30/40**.

---

## Skycrack

* Cast point reduced from **0.2** to **0.1**.
* Cooldown reduced from **4.5/4.0/3.5/3.0** to **4.00/3.25/2.50/1.75**.
* Range increased from **600** to **650**.
* Scepter cooldown reduced from **2.0** to **1.0**.

---

## Tesla Microarray

* Cooldown reduced from **80** to **25/20/15**.
* Damage increased from **140/200/260** to **325/400/475**.
* Radius reduced from **315** to **295**.
* Stun reduced from **2.00/2.75/3.50** to **1.50/1.75/2.00**.
* Chargetime reduced from **1.25** to **0.85**.

---

## war_berserker_aura

* Behavior changed from **DOTA_ABILITY_BEHAVIOR_PASSIVE/|/DOTA_ABILITY_BEHAVIOR_AURA** to **DOTA_ABILITY_BEHAVIOR_NO_TARGET**.
* Cast range reduced from **900** to **0**.
* Cast point increased from **0** to **0.2**.
* Cooldown increased from **0** to **15**.
* Mana cost increased from **0** to **155**.
* Radius reduced from **900** to **0**.
* Percent increased from **10** to **30/40/50/60**.

---

## Bloodlust

* Damage type changed from **DAMAGE_TYPE_PURE** to **DAMAGE_TYPE_MAGICAL**.
* Ao eradius increased from **275** to **375**.
* Cast range increased from **425** to **450**.
* Cooldown reduced from **20** to **14**.
* Mana cost reduced from **45/60/75/90** to **85**.
* Bonus attack speed increased from **30** to **50**.
* Var type changed from **FIELD_FLOAT** to **FIELD_FLOAT**.
* Radius increased from **275** to **375**.
* Duration reduced from **10.0** to **6.0**.
* Dot reduced from **15/25/35/45** to **10/15/20/25**.
* Linked special bonus changed from **special_bonus_war_3** to **special_bonus_war_3**.
* Slow increased from **15** to **15/20/25/30**.

---

## Earthbreaker

* Cast point increased from **0.38** to **0.42**.
* Cooldown reduced from **14/12/10/8** to **16**.
* Mana cost increased from **75** to **95**.
* Radius increased from **300** to **310**.
* Stun increased from **1.50** to **1.25/1.50/1.75/2.00**.

---

## war_enwrath


---

## war_fight_me

* Damage type changed from **DAMAGE_TYPE_PURE** to **DAMAGE_TYPE_MAGICAL**.
* Cooldown increased from **80** to **100/90/80**.
* Mana cost increased from **100** to **200**.
* Duration reduced from **2.75/3.25/4.00** to **3.5**.

---

## Warbellow


---

## Wrath


---

## npc_dota_hero_aeronaut

* Base strength increased from **19** to **21**.
* Strength gain increased from **1.2** to **1.7**.
* Base agility increased from **17** to **20**.
* Agility gain increased from **1.2** to **1.4**.

---

## npc_dota_hero_alexander

* 2 changed from **alexander_elandras_blessing** to **alexander_lightburst**.
* 3 changed from **alexander_radiant** to **alexander_raise_the_shield**.
* Armor physical reduced from **3** to **1**.
* Attack rate increased from **1.6** to **1.7**.
* Attack damage min increased from **23** to **24**.
* Attack damage max increased from **27** to **31**.
* Base strength increased from **23** to **32**.
* Strength gain increased from **2.0** to **3.4**.
* Base intelligence reduced from **17** to **12**.
* Intelligence gain increased from **1.75** to **1.9**.
* Base agility increased from **11** to **13**.

---

## npc_dota_hero_alroth

* Base strength increased from **23** to **25**.

---

## npc_dota_hero_apple

* 1 changed from **apple_strafe** to **apple_effigy_of_nature**.
* 2 changed from **apple_bouncing_arrow** to **apple_draining_arrow**.
* 3 changed from **apple_natures_blessing** to **apple_form_of_the_hawk**.
* 4 changed from **apple_corporeal_mine** to **apple_arrow_of_gaia**.

---

## npc_dota_hero_astaroth

* Base strength increased from **16** to **17**.
* Strength gain increased from **1.7** to **2**.

---

## npc_dota_hero_baal

* Movement turn rate rescaled from **0.7** to **0.7**.

---

## npc_dota_hero_bahamut

* Attack rate increased from **1.5** to **1.6**.
* Attack damage min reduced from **24** to **20**.
* Attack damage max reduced from **28** to **22**.
* Primary changed from **DOTA_ATTRIBUTE_AGILITY** to **DOTA_ATTRIBUTE_INTELLECT**.
* Base strength increased from **16** to **22**.
* Strength gain increased from **1.4** to **1.9**.
* Base intelligence increased from **15** to **33**.
* Intelligence gain increased from **1.7** to **2.8**.
* Base agility reduced from **23** to **20**.
* Agility gain increased from **2.2** to **2.8**.
* Movement speed reduced from **315** to **290**.

---

## npc_dota_hero_balthasar

* Armor physical increased from **0** to **1**.
* Attack damage min reduced from **28** to **25**.
* Attack damage max reduced from **29** to **28**.
* Movement speed reduced from **315** to **310**.
* Status health regen reduced from **1** to **0.5**.
* Status mana regen reduced from **1** to **0.5**.
* Vision nighttime range reduced from **1000** to **800**.

---

## npc_dota_hero_bloodwarrior

* Base strength increased from **22** to **23**.

---

## npc_dota_hero_chronos

* 2 changed from **chronos_** to **chronos_time_splicer**.
* 3 changed from **chronos_** to **chronos_chronoshock**.
* 4 changed from **chronos_time_splicer** to **chronos_convergence**.
* 16 changed from **attribute_bonus** to **special_bonus_chronos_3**.
* Attack rate increased from **1.5** to **1.6**.

---

## npc_dota_hero_cultist

* 6 changed from **cultist_chaos** to **cultist_sigil_of_decay**.

---

## npc_dota_hero_elementalist

* 1 changed from **elementalist_pillar_of_flame** to **elementalist_pillar_of_flame**.
* 2 changed from **elementalist_electric_whorl** to **elementalist_electric_whorl**.
* 3 changed from **elementalist_blizzard** to **elementalist_blizzard**.
* 4 changed from **elementalist_runic_detonation** to **elementalist_runic_detonation**.

---

## npc_dota_hero_elena

* Base strength increased from **14** to **17**.
* Strength gain increased from **1.7** to **1.9**.
* Base agility increased from **8** to **16**.
* Agility gain increased from **0.4** to **2**.

---

## npc_dota_hero_erra

* Intelligence gain increased from **1.7** to **2.2**.

---

## npc_dota_hero_fate

* 1 changed from **fate_displace** to **fate_displace**.
* 2 changed from **fate_chains_of_fate** to **fate_chains_of_fate**.
* 3 changed from **fate_realign** to **fate_realign**.
* 6 changed from **fate_ancestral_recall** to **fate_defiance**.
* 12 changed from **special_bonus_intelligence_8** to **special_bonus_attack_damage_40**.
* 15 changed from **special_bonus_fate_3** to **special_bonus_fate_2**.
* 16 changed from **special_bonus_fate_4** to **special_bonus_fate_3**.
* 17 changed from **special_bonus_spell_amplify_25** to **special_bonus_fate_4**.
* Strength gain increased from **1.0** to **1.7**.

---

## npc_dota_hero_feyguard

* 3 changed from **feyguard_unending** to **feyguard_retaliation_curse**.

---

## npc_dota_hero_fury

* 1 changed from **fury_roar** to **fury_roar**.
* 13 changed from **special_bonus_fury_2** to **special_bonus_fury_2**.
* 16 changed from **special_bonus_fury_3** to **special_bonus_fury_3**.
* 17 changed from **special_bonus_fury_4** to **special_bonus_fury_4**.

---

## npc_dota_hero_gemini

* Base strength increased from **15** to **19**.

---

## npc_dota_hero_gob_squad

* Armor physical increased from **2** to **15**.
* Base strength reduced from **17** to **12**.

---

## npc_dota_hero_hawkeye

* Base strength increased from **19** to **22**.

---

## npc_dota_hero_hero

* Attack range increased from **150** to **175**.
* Strength gain increased from **2.0** to **3.6**.
* Intelligence gain increased from **1.2** to **1.5**.
* Agility gain increased from **2.15** to **2.5**.

---

## The Lich

* Strength gain increased from **1.6** to **1.9**.

---

## npc_dota_hero_lightning

* 3 changed from **lightning_overload** to **lightning_spark**.
* 6 changed from **lightning_spark** to **lightning_overload**.
* Armor physical increased from **2** to **5**.
* Base strength increased from **19** to **23**.
* Strength gain increased from **1.5** to **2**.

---

## npc_dota_hero_lupin

* Attack damage min reduced from **31** to **25**.
* Attack damage max reduced from **38** to **29**.
* Base strength increased from **14** to **21**.
* Strength gain increased from **1.7** to **2.2**.
* Base intelligence reduced from **20** to **19**.
* Intelligence gain increased from **2.1** to **2.2**.
* Base agility increased from **15** to **27**.
* Agility gain increased from **1.6** to **2.7**.

---

## npc_dota_hero_lust

* Override hero changed from **npc_dota_hero_queen_of_pain** to **npc_dota_hero_queenofpain**.

---

## npc_dota_hero_pride

* Override hero changed from **npc_dota_hero_necrolyte** to **npc_dota_hero_phantom_lancer**.
* 1 changed from **pride_elyats_bellow** to **pride_elyats_bellow**.
* 2 changed from **pride_merciless** to **pride_merciless**.
* 3 changed from **pride_lionheart** to **pride_lionheart**.
* 6 changed from **pride_echospear** to **pride_echospear**.
* 10 changed from **special_bonus_attack_speed_25** to **special_bonus_attack_speed_25**.
* 11 changed from **special_bonus_pride_1** to **special_bonus_hp_regen_6**.
* 12 changed from **special_bonus_pride_2** to **special_bonus_pride_1**.
* 14 changed from **special_bonus_pride_3** to **special_bonus_pride_2**.
* 15 changed from **special_bonus_pride_4** to **special_bonus_pride_3**.
* 16 changed from **special_bonus_pride_5** to **special_bonus_pride_4**.
* 17 changed from **special_bonus_cooldown_reduction_20** to **special_bonus_pride_5**.
* Base strength reduced from **30** to **19**.
* Strength gain reduced from **2.5** to **2.3**.
* Base intelligence increased from **12** to **14**.
* Intelligence gain increased from **1.4** to **2.0**.
* Base agility reduced from **26** to **25**.
* Agility gain reduced from **2.9** to **2.3**.

---

## npc_dota_hero_rai

* Attack range increased from **150** to **175**.
* Base strength increased from **13** to **19**.
* Strength gain increased from **1.6** to **2.2**.
* Base intelligence increased from **19** to **20**.
* Intelligence gain increased from **2.2** to **2.3**.
* Movement speed reduced from **300** to **295**.

---

## npc_dota_hero_shade

* 3 changed from **shade_venomous** to **shade_shadowshift**.
* Strength gain increased from **1.7** to **2.2**.

---

## npc_dota_hero_shard_magus

* Strength gain increased from **1.3** to **1.8**.

---

## npc_dota_hero_siegfried

* Intelligence gain increased from **1.1** to **1.9**.

---

## npc_dota_hero_solstice


---

## npc_dota_hero_stoneforger


---

## npc_dota_hero_summoner


---

## npc_dota_hero_tek

* Armor physical increased from **1** to **4**.

---

## npc_dota_hero_teleri


---

## npc_dota_hero_war

* 3 changed from **war_berserker_aura** to **war_wrath**.
* 6 changed from **war_fight_me** to **war_warbellow**.
* Strength gain increased from **2.9** to **3.2**.
* Base intelligence increased from **16** to **17**.
* Intelligence gain increased from **1.5** to **1.9**.
* Base agility increased from **19** to **21**.
* Movement speed increased from **290** to **295**.
* Status health regen increased from **2** to **2.5**.
* Status mana regen reduced from **1** to **0.5**.

---

## Black Rose

* Bonus damage reduced from **20** to **15**.
* Active duration reduced from **2.25** to **1.5**.
* Active damage increase reduced from **15** to **12**.
* Max distance reduced from **1200** to **1000**.

---

## Crystal Focus

* Bonus spell a mp reduced from **10** to **7**.
* Mana percentage reduced from **70** to **35**.

---

## Seer's Lantern

* Slow increased from **25** to **30**.
* Magic res reduction increased from **20** to **30**.

---

## Wand of Yggdrasil

* Item requires charges increased from **0** to **1**.
* Item display charges increased from **0** to **1**.
* Hp drain reduced from **150** to **15**.
* Mp drain reduced from **150** to **15**.
* Hp percent drain reduced from **7** to **0.5**.
* Mp percent drain reduced from **7** to **0.25**.
* Delay reduced from **0.75** to **0.15**.