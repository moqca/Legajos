import wx
import wx.wizard as wiz
from xml.dom import minidom
import os
from elementtree.SimpleXMLWriter import XMLWriter
import sys
 
########################################################################
#
# New File WIZARD
########################################################################
class TitledPage(wiz.WizardPageSimple):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent, title):
        """Constructor"""
        wiz.WizardPageSimple.__init__(self, parent)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
 
        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        
        locationText = wx.StaticText(self, -1,                                 
                                'Selecciona la carpeta donde crear el proyecto')            
                                        
        self.locationBox = wx.TextCtrl(self, id=-1, size=wx.Size(100, 21))
        
        locationButton = wx.Button(id=-1, label=u'Browse',
              name=u'searchDir', parent=self, pos=wx.Point(152, 16),
              size=wx.Size(72, 26), style=0)
        
        projectNameText = wx.StaticText(self, -1,
                                'Por favor introduce el nombre de la empresa')
        self.projectName = wx.TextCtrl(self, id=-1, size=wx.Size(100, 21))
        
        self.fromTemplate = wx.CheckBox(self, -1, 'Crear desde Plantilla?')
        self.templateLocation = wx.TextCtrl(self, id=-1, size=wx.Size(100,21))
        self.templateLocation.Enable(False)
        
         
        #Binds
        locationButton.Bind(wx.EVT_BUTTON, self.on_search, id = -1)
        self.projectName.Bind(wx.EVT_TEXT, self.on_projectname, id = -1)
        self.fromTemplate.Bind(wx.EVT_CHECKBOX, self.on_check, id =-1)
        self.Bind(wiz.EVT_WIZARD_FINISHED, self.on_finish, id=-1)
        
        
        #Sizers
        sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(projectNameText, 0, wx.ALIGN_CENTRE | wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.projectName, 0, wx.ALIGN_CENTRE | wx.EXPAND | wx.ALL, 5)
        sizer.Add(locationText, 0, wx.ALIGN_LEFT, 5)
        sizer.Add(self.locationBox, 0, wx.ALIGN_CENTRE | wx.EXPAND | wx.ALL, 5)
        sizer.Add(locationButton, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        sizer.Add(self.fromTemplate, 0, wx.ALIGN_LEFT, 5)
        sizer.Add(self.templateLocation, 0, wx.EXPAND, 5)
        
        
    def on_search(self, event):
        dialog = wx.DirDialog (None, "Choose input directory", "",
                    wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            self.locationBox.SetValue(dialog.GetPath() + self.locationBox.GetValue())
            
        dialog.Destroy()
    
    def on_projectname(self, event):
        self.locationBox.SetValue('/' + self.projectName.GetValue().replace(" ",""))
        
    def on_check(self, event):
        self.templateLocation.Enable(self.fromTemplate.IsChecked())
        
    def on_finish(self, event):
        infodict = {}
        temp_name = ''.join([x for x in self.projectName.GetValue() if x.islower() or x.isupper()])
        infodict['name'] = temp_name
        infodict['path'] = self.locationBox.GetValue()
        infodict['templatePath'] = self.templateLocation.GetValue()
        return infodict
        
        
#----------------------------------------------------------------------

        
def new_project(tree):
    """"""
    wizard = wx.wizard.Wizard(None, -1, "Nueva Empresa")
    page1 = TitledPage(wizard, "Crear nueva empresa")

    wizard.FitToPage(page1)
    wizard.RunWizard(page1)
    info = page1.on_finish('e')
    wizard.Destroy()
    create_project(info['name'], info['path'])
    open_file(tree, info['path'])
    

def create_project(name, path, template=None):
    os.mkdir(path)
    os.mkdir(os.path.join(path, 'bin'))
    os.mkdir(os.path.join(path, 'contabilidad'))
    os.mkdir(os.path.join(path, 'documentos'))
    f = open(os.path.join(path, 'bin','empresa.xml'), 'w')
    w = XMLWriter(f)
    html = w.start("data")
    w.element("empresa", '"' + name + '"')
    w.start('items')
    w.element('item', nombre=name, indice='', parent='root')
    w.end('items')
    w.close(html)
    f.close()

    

########################################################################
## Open File Process
########################################################################

def open_file(tree, path=None):
    tree.DeleteAllItems()
    icons = Icon()
    tree.AssignImageList(icons.image_list)
    if path is None:
        xmldoc = minidom.parse('empresa.xml')
    else:
        xmldoc = minidom.parse(os.path.join(path, 'bin', 'empresa.xml'))
        

    itemlist = xmldoc.getElementsByTagName('item')
    tree_ids = {}
    for item in itemlist:
        parent = item.attributes['parent'].value
        name = item.attributes['nombre'].value
        index = item.attributes['indice'].value
        #resp = item.attributes['responsable'].value
        #review = item.attributes['reviso'].value
        #pend = item.attributes['pendientes'].value
        

        if parent == 'root':
            tree_id = tree.AddRoot('', 0)
            tree.SetItemText(tree_id, name, 1)
            tree_ids[name] = tree_id
            continue
        
        current = tree.AppendItem(tree_ids[parent], name, 1)
        tree.SetItemText(current, index, 0)
        #tree.SetItemText(current, resp, 2)
        #tree.SetItemText(current, review, 3)
        #tree.SetItemText(current, pend, 4)
        tree.SetItemText(current, name, 1)
        tree_ids[name] = current
        head, tail = os.path.splitext(name)
        
        tree.SetItemImage(current, icons.getImage(tail), wx.TreeItemIcon_Normal)

############################################################################
#   Save Project
############################################################################

def project_save1(tree):
    f = open('resar.xml', 'w')
    w = XMLWriter(f)
    html = w.start("data")
    w.element("empresa", '"' + tree.GetItemText(tree.GetRootItem(), 0) + '"')
    w.start('items')

    def printChildren(tree, treeItem):
        subItem = tree.GetFirstChild(treeItem)[0]
        name = tree.GetItemText(treeItem, 1)
        index = tree.GetItemText(treeItem, 0)
        try:
            parent = tree.GetItemText(tree.GetItemParent(treeItem), 1)
        except Exception:
            parent = 'root'

        if not subItem.IsOk():
            w.element("item", nombre=name, indice=index, parent=parent)

        else:
            w.element("item", nombre=name, indice=index, parent='root')

        while subItem.IsOk():
            printChildren(tree, subItem)
            subItem = tree.GetNextSibling(subItem)

    printChildren(tree, tree.GetRootItem())
   
    w.end('items')
    w.close(html)
    f.close()


def project_save(tree):
    e = open('resio.xml', 'w')
    
    def printChildren(tree, treeItem, indent=0):
        subItem = tree.GetFirstChild(treeItem)[0]
        name, ext = os.path.splitext(tree.GetItemText(treeItem))

        if not subItem.IsOk() and ext:
            e.write("  " * indent + "- " + tree.GetItemText(treeItem) + "-" + tree.GetItemText(tree.GetItemParent(treeItem)) + "\n")
        else:
            e.write('item project=' + tree.GetItemText(treeItem) + ' blah = root')
            # e.write("  " * indent + tree.GetItemText(treeItem) + ":\n" )
        while subItem.IsOk():
            printChildren(tree, subItem, indent + 1)
            subItem = tree.GetNextSibling(subItem)

    printChildren(tree, tree.GetRootItem())
    e.close()

############################################################################
#   Pretty Icons
############################################################################

class Icon():
    def __init__(self):
        self.image_list = wx.ImageList(16, 16)
        self.match = {}

    def create_image(self, type):
        try:
            return self.match[type]
        except Exception:
            for i in os.listdir('small'):
                if type in i:
                     name, ext = os.path.splitext(i)
                     self.match[name] = self.image_list.Add(wx.Image("small/" + i, wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())


    def getImage(self, type):
        if type == '':
            type = 'Folder-icon'
        try:
            return self.match[type]
        except Exception:
            try:
                self.create_image(type)
                return self.match[type]
            except Exception:
                self.create_image('genericBlue')
                return self.match['genericBlue']






########################################################################
# Main



if __name__ == "__main__":
    app = wx.App(False)
    app.MainLoop()