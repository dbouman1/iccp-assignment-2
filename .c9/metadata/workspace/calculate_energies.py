{"filter":false,"title":"calculate_energies.py","tooltip":"/calculate_energies.py","undoManager":{"mark":6,"position":6,"stack":[[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["\\"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["\\"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":3},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":24},"end":{"row":6,"column":30},"action":"remove","lines":["reviou"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["o"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["s"]},{"start":{"row":8,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    ","","","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":26},"end":{"row":5,"column":45},"action":"remove","lines":["_nodal_points, angl"]},{"start":{"row":5,"column":26},"end":{"row":6,"column":94},"action":"insert","lines":["sible_beads_pos,beads_pos,epsilon,sigma):","    energies  = np.zeros(len(possible_beads_pos),dtype=float) # initialize all possible energi"]},{"start":{"row":6,"column":96},"end":{"row":6,"column":97},"action":"remove","lines":[","]},{"start":{"row":6,"column":98},"end":{"row":8,"column":0},"action":"remove","lines":["hain_length):","    energies  = np.zeros(len(angles),dtype=float)",""]},{"start":{"row":6,"column":98},"end":{"row":13,"column":36},"action":"insert","lines":["orresponding to each possible new bead position","    for ii in range(0, len(possible_beads_pos)-1):","        for iii in range(0,len(beads_pos)-1):","            abs_distance_squared = np.divide(sum(np.square(np.subtract(possible_beads_pos[ii,:],beads_pos[iii,:]))),np.square(sigma)) # distance alluar","            V = 4*epsilon*(np.power(abs_distance_squared,-6)-np.power(abs_distance_squared,-3))","            energies[ii] = energies[ii]+V","","    energies = np.divide(energies,2)"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":20},"end":{"row":8,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1426169412000,"hash":"2be16a1b9b89aa004cf7800126fcbdbd77ecfc1f"}