##
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos from the user. Then your program should compute
# and display the total weight of the parts.
#              
#

WIDG_WEIGHT = 75
GIZ_WEIGHT = 112

widgets = int( input("Inserisci il numero di widgets: ") )
gizmos = int( input("Inserisci il numero di gizmos: ") )

total_weight = widgets * WIDG_WEIGHT + gizmos * GIZ_WEIGHT

print("Il peso totale dei tuoi widgets e gizmos è:", total_weight , "grammi")