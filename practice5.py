# 패키지

from travel import thailand
thailand.ThailandPackage()

from travel import vietnam
vietnam.VietnamPackage()

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

import travel.vietnam
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to2 = thailand.ThailandPackage()
trip_to2.detail()

# Quiz 10

import byme
byme.sign()

