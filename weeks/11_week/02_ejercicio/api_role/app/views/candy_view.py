
#marca, peso, sabor, origen
#brand, weight, taste, origin
def render_candy_list(candys):
    return [
        {
            "id": candy.id,
            "brand": candy.brand,
            "weight": candy.weight,
            "taste": candy.taste,
            "origin": candy.origin,
        }
        for candy in candys
    ]

def render_candy_detail(candy):
    return {
        "id": candy.id,
        "brand": candy.brand,
        "weight": candy.weight,
        "taste": candy.taste,
        "origin": candy.origin,
    }
