#Boa:Frame:Frame1
import wxversion

wxversion.select('2.9.3')

import wx
from wx.lib.anchors import LayoutAnchors
import wx.gizmos
import project_handle
import financial_parser
import os
import shutil

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BALANCETREE, wxID_FRAME1BOTTOMBOOK, 
 wxID_FRAME1BOTTOMCONTENT, wxID_FRAME1BOTTOMNOTES, wxID_FRAME1CONTENTBOOK, 
 wxID_FRAME1CONTENTCONTAINER, wxID_FRAME1CONTENTSPLITTER, wxID_FRAME1FILETREE, 
 wxID_FRAME1FILETREECONTAINER, wxID_FRAME1PANEL1, wxID_FRAME1SPLITTERWINDOW1, 
 wxID_FRAME1TOOLBAR1, wxID_FRAME1TOPCONTENT, 
] = [wx.NewId() for _init_ctrls in range(14)]

[wxID_FRAME1MENU1NEWFILE, wxID_FRAME1MENU1OPENFILE, 
 wxID_FRAME1MENU1SAVEASFILE, wxID_FRAME1MENU1SAVEFILE, 
] = [wx.NewId() for _init_coll_Archivo_Items in range(4)]

[wxID_FRAME1TOOLBAR1IMPCONTAB, wxID_FRAME1TOOLBAR1NEWFOLDER, 
 wxID_FRAME1TOOLBAR1TOOLABRIR, wxID_FRAME1TOOLBAR1TOOLCREATE, 
 wxID_FRAME1TOOLBAR1TOOLGUARDAR, wxID_FRAME1TOOLBAR1TOOLSAVEAS, 
] = [wx.NewId() for _init_coll_toolBar1_Tools in range(6)]

class Frame1(wx.Frame):
    def _init_coll_bottomContentSizer_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.bottomBook, 1, border=0, flag=wx.EXPAND)

    def _init_coll_contentSizer_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.contentSplitter, 1, border=0, flag=wx.EXPAND)

    def _init_coll_boxSizer3_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.fileTree, 1, border=0, flag=wx.EXPAND)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.toolBar1, 0, border=0, flag=wx.GROW)
        parent.AddWindow(self.splitterWindow1, 1, border=0, flag=wx.EXPAND)

    def _init_coll_boxSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.contentBook, 1, border=0, flag=wx.EXPAND)

    def _init_coll_Archivo_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENU1NEWFILE, kind=wx.ITEM_NORMAL,
              text=u'Nuevo')
        parent.Append(help=u'', id=wxID_FRAME1MENU1OPENFILE,
              kind=wx.ITEM_NORMAL, text=u'Abrir')
        parent.Append(help='', id=wxID_FRAME1MENU1SAVEFILE, kind=wx.ITEM_NORMAL,
              text=u'Save')
        parent.Append(help='', id=wxID_FRAME1MENU1SAVEASFILE,
              kind=wx.ITEM_NORMAL, text=u'Save As')

    def _init_coll_MainMenu_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.Archivo, title=u'Archivo')

    def _init_coll_fileTree_Columns(self, parent):
        # generated method, don't edit

        parent.AddColumn(text=u'Ind')
        parent.AddColumn(text=u'Nombre')

    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'images/door--plus.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1TOOLCREATE, kind=wx.ITEM_NORMAL, label=u'',
              longHelp=u'', shortHelp=u'Crear un nuevo proyecto')
        parent.DoAddTool(bitmap=wx.Bitmap(u'images/door-open.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1TOOLABRIR, kind=wx.ITEM_NORMAL, label='',
              longHelp='', shortHelp=u'Abrir proyecto')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wx.Bitmap(u'images/disk.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1TOOLGUARDAR, kind=wx.ITEM_NORMAL, label='',
              longHelp='', shortHelp=u'Guardar el pryecto Actual')
        parent.DoAddTool(bitmap=wx.Bitmap(u'images/disks.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1TOOLSAVEAS, kind=wx.ITEM_NORMAL, label='',
              longHelp='', shortHelp=u'Guardar Como ...')
        parent.AddSeparator()
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wx.Bitmap(u'images/folder-sticky-note.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1NEWFOLDER, kind=wx.ITEM_NORMAL,
              label=u'Nuevo Folder', longHelp=u'',
              shortHelp=u'Crea un Nuevo Folder')
        parent.DoAddTool(bitmap=wx.Bitmap(u'images/box--plus.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_FRAME1TOOLBAR1IMPCONTAB, kind=wx.ITEM_NORMAL, label='',
              longHelp=u'', shortHelp=u'Importar Informacion Contable')
        self.Bind(wx.EVT_TOOL, self.On_new_file,
              id=wxID_FRAME1TOOLBAR1TOOLCREATE)
        self.Bind(wx.EVT_TOOL, self.On_tool_open,
              id=wxID_FRAME1TOOLBAR1TOOLABRIR)
        self.Bind(wx.EVT_TOOL, self.on_tool_save,
              id=wxID_FRAME1TOOLBAR1TOOLGUARDAR)
        self.Bind(wx.EVT_TOOL, self.On_new_doc_folder,
              id=wxID_FRAME1TOOLBAR1NEWFOLDER)
        self.Bind(wx.EVT_TOOL, self.On_import_contab,
              id=wxID_FRAME1TOOLBAR1IMPCONTAB)

        parent.Realize()

    def _init_coll_bottomBook_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.bottomNotes, select=True,
              text=u'Notas')

    def _init_coll_contentBook_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.balanceTree, select=True,
              text=u'Balance General')

    def _init_coll_balanceTree_Columns(self, parent):
        # generated method, don't edit

        parent.AddColumn(text=u'No. de Cuenta')
        parent.AddColumn(text=u'Descripcion')
        parent.AddColumn(text=u'Saldo Mes Anterior')
        parent.AddColumn(text=u'Cargos')
        parent.AddColumn(text=u'Abonos')
        parent.AddColumn(text=u'Saldo')

        parent.SetColumnAlignment(0, wx.gizmos.TL_ALIGN_RIGHT)
        parent.SetColumnAlignment(1, wx.gizmos.TL_ALIGN_RIGHT)
        parent.SetColumnAlignment(2, wx.gizmos.TL_ALIGN_RIGHT)
        parent.SetColumnAlignment(3, wx.gizmos.TL_ALIGN_RIGHT)

    def _init_utils(self):
        # generated method, don't edit
        self.Archivo = wx.Menu(title=u'')

        self.MainMenu = wx.MenuBar()

        self._init_coll_Archivo_Items(self.Archivo)
        self._init_coll_MainMenu_Menus(self.MainMenu)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.contentSizer = wx.BoxSizer(orient=wx.VERTICAL)

        self.boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)

        self.bottomContentSizer = wx.BoxSizer(orient=wx.VERTICAL)

        self.boxSizer3 = wx.BoxSizer(orient=wx.VERTICAL)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_contentSizer_Items(self.contentSizer)
        self._init_coll_boxSizer2_Items(self.boxSizer2)
        self._init_coll_bottomContentSizer_Items(self.bottomContentSizer)
        self._init_coll_boxSizer3_Items(self.boxSizer3)

        self.contentContainer.SetSizer(self.contentSizer)
        self.panel1.SetSizer(self.boxSizer1)
        self.fileTreeContainer.SetSizer(self.boxSizer3)
        self.topContent.SetSizer(self.boxSizer2)
        self.bottomContent.SetSizer(self.bottomContentSizer)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(442, 109), size=wx.Size(923, 719),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self._init_utils()
        self.SetClientSize(wx.Size(915, 692))
        self.SetMenuBar(self.MainMenu)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(915, 692),
              style=wx.TAB_TRAVERSAL)

        self.splitterWindow1 = wx.SplitterWindow(id=wxID_FRAME1SPLITTERWINDOW1,
              name='splitterWindow1', parent=self.panel1, pos=wx.Point(0, 28),
              size=wx.Size(915, 664), style=wx.SP_3D)
        self.splitterWindow1.SetSashSize(4)
        self.splitterWindow1.SetMinimumPaneSize(120)
        self.splitterWindow1.SetMinSize(wx.Size(-1, -1))

        self.fileTreeContainer = wx.Panel(id=wxID_FRAME1FILETREECONTAINER,
              name=u'fileTreeContainer', parent=self.splitterWindow1,
              pos=wx.Point(2, 2), size=wx.Size(251, 660),
              style=wx.TAB_TRAVERSAL)

        self.contentContainer = wx.Panel(id=wxID_FRAME1CONTENTCONTAINER,
              name=u'contentContainer', parent=self.splitterWindow1,
              pos=wx.Point(257, 2), size=wx.Size(656, 660),
              style=wx.TAB_TRAVERSAL)
        self.splitterWindow1.SplitVertically(self.fileTreeContainer,
              self.contentContainer, 253)

        self.toolBar1 = wx.ToolBar(id=wxID_FRAME1TOOLBAR1, name='toolBar1',
              parent=self.panel1, pos=wx.Point(0, 0), size=wx.Size(915, 28),
              style=wx.TB_HORIZONTAL | wx.NO_BORDER)

        self.contentSplitter = wx.SplitterWindow(id=wxID_FRAME1CONTENTSPLITTER,
              name=u'contentSplitter', parent=self.contentContainer,
              pos=wx.Point(0, 0), size=wx.Size(656, 660), style=wx.SP_3D)
        self.contentSplitter.SetLabel(u'contentSplitter')
        self.contentSplitter.SetMinimumPaneSize(2)
        self.contentSplitter.SetMinSize(wx.Size(-1, -1))
        self.contentSplitter.SetToolTipString(u'contentSplitter')
        self.contentSplitter.SetSashSize(5)

        self.topContent = wx.Panel(id=wxID_FRAME1TOPCONTENT, name=u'topContent',
              parent=self.contentSplitter, pos=wx.Point(2, 2), size=wx.Size(652,
              463), style=wx.TAB_TRAVERSAL)
        self.topContent.SetToolTipString(u'TopContent')

        self.bottomContent = wx.Panel(id=wxID_FRAME1BOTTOMCONTENT,
              name=u'bottomContent', parent=self.contentSplitter,
              pos=wx.Point(2, 470), size=wx.Size(652, 188),
              style=wx.TAB_TRAVERSAL)
        self.contentSplitter.SplitHorizontally(self.topContent,
              self.bottomContent, 465)

        self.contentBook = wx.Notebook(id=wxID_FRAME1CONTENTBOOK,
              name=u'contentBook', parent=self.topContent, pos=wx.Point(0, 0),
              size=wx.Size(652, 463), style=wx.NO_BORDER)

        self.balanceTree = wx.gizmos.TreeListCtrl(id=wxID_FRAME1BALANCETREE,
              name=u'balanceTree', parent=self.contentBook, pos=wx.Point(0, 0),
              size=wx.Size(644, 437),
              style=wx.TR_ROW_LINES | wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT)
        self._init_coll_balanceTree_Columns(self.balanceTree)

        self.bottomBook = wx.Notebook(id=wxID_FRAME1BOTTOMBOOK,
              name=u'bottomBook', parent=self.bottomContent, pos=wx.Point(0, 0),
              size=wx.Size(652, 188), style=0)

        self.bottomNotes = wx.TextCtrl(id=wxID_FRAME1BOTTOMNOTES,
              name=u'bottomNotes', parent=self.bottomBook, pos=wx.Point(0, 0),
              size=wx.Size(644, 162), style=0, value=u'')

        self.fileTree = wx.gizmos.TreeListCtrl(id=wxID_FRAME1FILETREE,
              name=u'fileTree', parent=self.fileTreeContainer, pos=wx.Point(0,
              0), size=wx.Size(251, 660),
              style=wx.TR_EDIT_LABELS | wx.TR_HAS_BUTTONS)
        self.fileTree.SetIndent(5)
        self.fileTree.SetLabel(u'fileTree')
        self.fileTree.SetLineSpacing(7)
        self.fileTree.SetMainColumn(1)
        self.fileTree.SetHelpText(u'')
        self._init_coll_fileTree_Columns(self.fileTree)

        self._init_coll_toolBar1_Tools(self.toolBar1)
        self._init_coll_contentBook_Pages(self.contentBook)
        self._init_coll_bottomBook_Pages(self.bottomBook)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        
            	#########Icon Test
    	self.icons = Icon()
    	self.fileTree.AssignImageList(self.icons.image_list)
    	###########
    	
        self.droptarget = FileDrop(self.fileTree, self.fileTree.GetRootItem(), self.icons)
        self.fileTree.SetDropTarget(self.droptarget)
        self.fileTree.Bind(wx.EVT_TREE_BEGIN_DRAG, self.OnBeginDrag)
    	self.fileTree.Bind(wx.EVT_TREE_END_DRAG, self.OnEndDrag)
    	

        

    def On_new_file(self, event):
        dialog = wx.MessageDialog (None, "Cerrar el proyecto Actual?", "",
                    wx.YES_NO)
        if dialog.ShowModal() == wx.ID_YES:
            project_handle.new_project(self.fileTree)

    def On_tool_open(self, event):
        self.fileTree.DeleteAllItems()
        dlg = wx.DirDialog(self, "Elige el Dierctorio:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        
        path = None
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        dlg.Destroy()
        
        project_handle.open_file(self.fileTree, path)
        self.root = self.fileTree.GetRootItem()
        self.fileTree.ExpandAll(self.root)
        
        financialInformation = financial_parser.Finance(self.balanceTree, path)
        financialInformation.load_financials()

    def on_tool_save(self, event):
        project_handle.project_save1(self.fileTree)

    def On_new_doc_folder(self, event):
        dlg = wx.TextEntryDialog(None, "Por favor introduce el indice")
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            if dlg.GetValue() != '':
                self.fileTree.AppendItem(self.root, dlg.GetValue(), 0)
            else:
                warningDlg = wx.Dialog(None, 'Favor de introducir Indice')
        dlg.Destroy()
        
    def OnBeginDrag(self, event):
        '''Allow drag-and-drop for leaf nodes.'''
        #self.log.WriteText("OnBeginDrag")

        if self.fileTree.GetChildrenCount(event.GetItem()) == 0:
            event.Allow()
            self.dragItem = event.GetItem()
        else:
            #self.log.WriteText("Cant drag a node that has children")
            pass


    def OnEndDrag(self, event):
        '''Do the re-organization if possible'''

        #self.log.WriteText("OnEndDrag")
       #If we dropped somewhere that isn't on top of an item, ignore the event

        if not event.GetItem().IsOk():
            return

        # Make sure this memeber exists.
        try:
            old = self.dragItem
        except:
            return

        # Get the other IDs that are involved
        new = event.GetItem()
        fnam, ext = os.path.splitext(self.fileTree.GetItemText(new))
        parent = self.fileTree.GetItemParent(new)

        if not parent.IsOk() or ext:
            return

        # Move 'em

        index = self.fileTree.GetItemText(old)
        text = self.fileTree.GetItemText(old, 1)
        self.fileTree.Delete(old)
        do = self.fileTree.AppendItem(new, index)
        self.fileTree.SetItemText(do, text, 1)
        head, tail = os.path.split(text)
        n, ext = os.path.splitext(tail)

        #self.fileTree.SetItemImage(do, self.fileTree.d.getImage(ext[1:]), wx.TreeItemIcon_Normal)
        self.fileTree.ExpandAll(self.root)

    def On_import_contab(self, event):
        event.Skip()
        
class FileDrop(wx.FileDropTarget):
    def __init__(self, window, root, images):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.root = root
        self.images = images
        
        
    def OnDropFiles(self, x, y, filenames):
        new = self.window.HitTest((x, y))[0]
        new = self.window.GetItemParent(new)
        
        filenames.sort()
        for name in filenames:
            try:
                (head, tail) = os.path.split(name)
                if not os.path.exists('documentos/'):
                    os.mkdir('documentos/')
                shutil.copy2(name, os.path.join('documentos/', tail))
                last = self.window.GetLastChild(new)
                
                try:
                    text = self.window.GetItemText(self.window.GetLastChild(new)[0], 0)
                    newIndex = text[:text.index('.')+1] + str(int(text[text.index('.')+1:]) + 1)
                    newItem = self.window.AppendItem(new, newIndex)
                except Exception, e:
                    print e
                    newItem = self.window.AppendItem(new, 'XX')

                self.window.SetItemText(newItem, tail, 1)
                self.window.SetPyData(newItem, None)
                n, ext = os.path.splitext(tail)
                
                if os.path.isfile(name):
                    self.window.SetItemImage(newItem, self.images.getImage(ext[:1]), wx.TreeItemIcon_Normal)
                    #self.window.SetItemImage(newItem, 1, wx.TreeItemIcon_Normal)
                else:
                    self.window.SetItemImage(newItem, self.images.getImage('Folder-icon'), wx.TreeItemIcon_Normal)
                    
            except IOError as error:
                dlg = wx.MessageDialog(None, "Error opening file \n" + str(error))
                dlg.ShowModal()
            except UnicodeDecodeError as error:
                dlg = wx.MessageDialog(None, "No se puede abrir el archivo con ese nombre \n" + str(error))
                dlg.ShowModal()

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
