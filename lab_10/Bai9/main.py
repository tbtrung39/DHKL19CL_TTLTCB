from qlyhanghoa import input_items, compute_amounts, sort_by_vat_desc, print_items


def main():
    items = input_items()
    print('\n--- Trước khi sắp xếp ---')
    print_items(items)
    compute_amounts(items)
    sorted_items = sort_by_vat_desc(items)
    print('\n--- Sau khi sắp xếp giảm dần theo Thuế ---')
    print_items(sorted_items)


if __name__ == '__main__':
    main()
