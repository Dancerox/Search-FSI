# Search methods

import search


ab = search.GPSProblem('A', 'B', search.romania)
sg = search.GPSProblem('S', 'G', search.romania)
tp = search.GPSProblem('T', 'P', search.romania)

#print "Busqueda en anchura"
#print search.breadth_first_graph_search(ab).path()

#print "Busqueda en profundidad"
#print search.depth_first_graph_search(ab).path()


print "Ramificacion y acotacion"
print search.RamificacionAcotacion(ab).path()

print "Ramificacion y acotacion con heuristica"
print search.RamificacionAcotacionHeuristica(ab).path()



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
