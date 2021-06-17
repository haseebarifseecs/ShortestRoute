def calculate_shortest_airport_route(Airports, Source, Destination):
  nodes = {} # Key: Node Value:Weight
  updates = {} #Nodes whose weights are updated
  nodesProps = dict() #Contains Undirected Connected Routes
  for i in airports:
    if i.get("start") not in nodesProps.keys():
      nodesProps[i.get("start")] = {
          "adjacent":{
              i.get("end"):i.get("cost")
          }
      }
    else:
      nodesProps[i.get("start")].get("adjacent").update(
          {
              i.get("end"):i.get("cost")
          }
      )
    if i.get("end") not in nodesProps.keys():
      nodesProps[i.get("end")] = {
          "adjacent":{
              i.get("start"):i.get("cost")
          }
      }
    else:
      nodesProps[i.get("end")].get("adjacent").update(
          {
              i.get("start"):i.get("cost")
          }
      )

  print(nodesProps)
  for item in nodesProps.keys():
    if ( item == source): nodes[item] = 0 #Source Node is always given initial Weight = 0
    else: nodes[item] = float('inf') #All other nodes from initial Node are given infinite weight 
  print(nodes)
  visited = dict() #Holds Duplicate of Nodes 
  for i in nodes.keys():
      visited[i] = nodes[i]
  while (len(visited) > 0): #Loop till all nods are visited
    minNode = min(visited, key=visited.get) #Determine Node with minimum Weight
    #print(minNode)
    for i in nodesProps[minNode]['adjacent']: #Loops through Nodes adjacent to Source Node
      if (nodes[i] > ( nodes[minNode] + nodesProps[minNode]['adjacent'][i] )): #If Connected Nodes weights is greater than the combined weight of Initial Node and the actual weight in adjacent Edges
          nodes[i] = nodes[minNode] + nodesProps[minNode]['adjacent'][i] #Updating Weights
          visited[i] = nodes[minNode] + nodesProps[minNode]['adjacent'][i] #Also Storing Updated Information in Visited Nodes
          updates[i] = minNode #Holds which node is updated 
    del visited[minNode] #Deleting the node which has been visited 
  #Reverse Tracking to Print Path  
  temp = destination
  routes = []
  paths = []
  while True:
    routes.append(temp)
    if temp in updates: temp = updates[temp] #Tracking in Reverse i.e from dest to source
    else: return 0
    if temp == source:
      routes.append(temp)
      break
  for j in range(len(routes)-1,-1,-1):
        paths.append(routes[j])
  cost = nodes[destination]

  return cost ,paths  

#Inputs
airports = [
	 {
		 'start': 'ISB',
		 'end': 'LHR',
		 'cost': 1000
	 },
	 {
		 'start': 'LHR',
		 'end': 'NYC',
		 'cost': 750
	 },
	 {
		 'start': 'CBS',
		 'end': 'NYC',
		 'cost': 775
	 },
	 {
		 'start': 'ISB',
		 'end': 'CBS',
		 'cost': 575
	 },
	 {
		 'start': 'CBS',
		 'end': 'GRC',
		 'cost': 731
	 },
	 {
		 'start': 'NYC',
		 'end': 'GRC',
		 'cost': 459
	 }
 ]

source = "ISB"
destination = "NYC"

print(f'Output: {calculate_shortest_airport_route(airports,source,destination)}')
