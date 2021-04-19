# coding=utf-8
import re

text = """
//
//  ContentView.swift
//  Devote
 

import SwiftUI
import CoreData

struct ContentView: View {
    // MARK : - property
    
    @State var task: String = ""
    @State private var showNewTaskItem: Bool = false
    
    // fetching data
    @Environment(\.managedObjectContext) private var viewContext

    @FetchRequest(
        sortDescriptors: [NSSortDescriptor(keyPath: \Item.timestamp, ascending: true)],
        animation: .default)
    private var items: FetchedResults<Item>
    
    // MARK : function
    

    private func deleteItems(offsets: IndexSet) {
        withAnimation {
            offsets.map { items[$0] }.forEach(viewContext.delete)

            do {
                try viewContext.save()
            } catch {
         
                let nsError = error as NSError
                fatalError("Unresolved error \(nsError), \(nsError.userInfo)")
            }
        }
    }

    // MARK: - body

    var body: some View {
        NavigationView {
            ZStack {
                
                // MARK: - MAIN
                VStack {
                    // MARK: - head
                    
                    Spacer(minLength: 80)
                    
                    // MARK: - new task
                    
                    Button(action: {
                        showNewTaskItem = true
                    }, label: {
                        Image(systemName: "plus.circle")
                            .font(.system(size:30,weight:.bold,design:.rounded))
                        Text("New Task")
                            .font(.system(size:24,weight:.bold,design:.rounded))
                            .foregroundColor(.white)
                            

                    })
                    .padding(.horizontal, 20)
                    .padding(.vertical, 15)
                    .background(LinearGradient(gradient: Gradient(colors: [Color.pink, Color.blue]), startPoint: .leading, endPoint: .trailing))
                    .clipShape(Capsule())
                    .shadow(color: Color(red: 0, green: 0, blue: 0), radius: 8, x: 0, y: 4.0)
                    
                    
                    // MARK: - task
                    
                    List {
                        ForEach(items) { item in
                            VStack(alignment: .leading) {
                                Text(item.task ?? "")
                                    .font(.headline)
                                    .fontWeight(.bold)
                                Text("Item at \(item.timestamp!, formatter: itemFormatter)")
                                    .font(.footnote)
                                    .foregroundColor(.gray)
                            } // vstack
                        }
                        .onDelete(perform: deleteItems)
                    }//: LIST
                    .listStyle(InsetGroupedListStyle())
                    .shadow(color: Color(red: 0, green: 0, blue: 0, opacity: 0.3), radius: 12 )
                    .padding(.vertical, 0)
                    .frame(maxWidth: 640)
                }// vstack
                
                
                // MARK: - new task item
                
                if showNewTaskItem {
                    BlankView()
                        .onTapGesture {
                            withAnimation {
                                showNewTaskItem = false
                            }
                        }
                    
                    NewTaskActionView()
                }
                
                
            }//： zstack
            .onAppear(){
                UITableView.appearance().backgroundColor = UIColor.clear
            }
            .navigationBarTitle("Daily Tasks", displayMode: .large)
            .toolbar {
                #if os(iOS)
                ToolbarItem(placement: .navigationBarTrailing){
                    EditButton()
                }
                #endif
            } //: TODlbar
            .background(
                BackgroundImageView()
            )
            .background(backgroundGradient.ignoresSafeArea())
        } //: navation
        .navigationViewStyle(StackNavigationViewStyle())
        
        }
    }

//


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
                rel = re.search('(.*)? \\{', ocl).groups("1")[0].strip().split(" ")[-1]
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
