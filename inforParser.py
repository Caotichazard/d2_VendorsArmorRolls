import itens


def parse_items(info,vendor,charClass):
    item_indexes = itens.item_index_dict[vendor][charClass]
    items_info = {}
    items_info["class"] = charClass
    items_info["vendor"] = vendor
    items_info["items"] = {}
    for item,index in item_indexes.items():
        item_stats = info[index]["stats"]
        temp = {}
        stat_total = 0
        for stat_hash,stat in itens.armor_stats.items():
            stat_value = item_stats[stat_hash]["value"]
            stat_total += stat_value
            temp[stat] = stat_value
        temp["stat_total"] = stat_total
        items_info["items"][item] = temp
    
    print(items_info)