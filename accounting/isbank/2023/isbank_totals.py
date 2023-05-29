# a function with the same name exists under yapikredi/2023
# kavunici
def total_cost_courier(courier_count, gas_price, currency):
    vehicles = courier_count * 1.2

    try_cost_mon = vehicles * gas_price * 30
    dollar_cost_mon = try_cost_mon * 19.5
    eur_cost_mon = try_cost_mon * 20.5

    if currency == "try":
        return try_cost_mon
    elif currency == "eur":
        return eur_cost_mon
    elif currency == "dollar":
        return dollar_cost_mon
    

def get_grouped_float4_idxs(acc:List[Token]) -> Optional[List[int]]:
  idxs: Optional[List[int]] = []
  for i,a in enumerate(acc):
    if idxs is None: break
    if i in idxs: continue
    if a.ltype == LocalTypes.float4 and a.offset == 0:
      idxs.append(i)
      friends: List[int] = []
      for j,b in enumerate(acc):
        if len(friends) == 3: break
        if j in idxs: continue
        if a.name == b.name and b.ltype == LocalTypes.float4 and b.offset == len(friends)+1:
          friends.append(j)
      if len(friends) == 3: idxs += friends
      else: idxs = None
    else:
      idxs = None
  return idxs

def to_float4(x:List[Token]) -> Optional[Token]:
  if all_same(x): return x[0]
  if all_same([y.name for y in x]) and all([y.ltype == LocalTypes.float4 and y.offset == i for i,y in enumerate(x)]):
    return Token(x[0].name, LocalTypes.float4)
  return None

def get_grouped_maybe_float4(*values:List[Token], grouping_allowed=True):
  assert all_same([len(x) for x in values]), f"all values are not the same length {values}"
  # these use accumulators, we can only fold if the acc is a float4
  idxs = get_grouped_float4_idxs(values[0]) if grouping_allowed else None
  if idxs is not None:
    new_idxs = []
    new_values = []
    for i in range(0, len(idxs), 4):
      nv = [to_float4([v[j] for j in idxs[i:i+4]]) for v in values]
      if any([x is None for x in nv]): break
      new_idxs.append(idxs[i:i+4])
      new_values.append(nv)
    if len(new_values) == len(idxs)//4:
      return zip(new_idxs, new_values)
  return zip([[i] for i in range(len(values[0]))], zip(*values))
