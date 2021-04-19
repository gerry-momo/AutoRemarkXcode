# coding=utf-8
import re

text = """
//
//  ContentView.swift
//  Devote
 

import SwiftUI
import CoreData

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView().environment(\.managedObjectContext, PersistenceController.preview.container.viewContext)
    }
}

"""


def mark_it(path):
    with open(path, 'r') as f:
        ftext = "".join(f.readlines())

    origin_code_list = ftext.split('\n')
    new_code_list = []
    wait_mark = []

    for ocl in origin_code_list:

        if "{" in ocl and "}" in ocl:
            new_code_list.append(ocl)
            continue

        if "{" in ocl:
            # print(ocl)
            try:
                tmp_ocl = re.sub(r'\((.*?)\)', '', ocl)
                rel = re.search('(.*)? \\{', tmp_ocl).groups("1")[0].strip().split(" ")[-1]
            except:
                rel = ocl.split("{")[0].strip().split(" ")[-1]
            wait_mark.append(rel)
            new_code_list.append(ocl)
            continue

        if "}" in ocl:
            # 先清理原始备注
            ocl = ocl if "//" not in ocl else "".join(ocl.split('//')[0:-1])
            ocl = ocl + f" // {wait_mark[-1]}"
            wait_mark.pop(-1)
            new_code_list.append(ocl)
            continue

        new_code_list.append(ocl)

    new_code = "\n".join(new_code_list)
    with open(path, 'w') as f:
        f.write(new_code)

    return True


if __name__ == '__main__':
    mark_it(text)
