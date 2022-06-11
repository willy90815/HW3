

class PageManager:
    def __init__(self,line,frame_size):
        self.page_list = line.removesuffix("\n")
        self.reslut_string = ''
        self.frame_size = int(frame_size)
    def FIFO(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------FIFO-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
                if len(frame)>self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)
        print(self.reslut_string)
    
    def LRU(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------LRU-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
                if len(frame)>self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
            else:
                frame.remove(i)
                frame.insert(0,i)

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)
        print(self.reslut_string)

    
    def LFU_LRU(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------LFU_LRU-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
                if len(frame)>self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
            else:
                frame.remove(i)
                frame.insert(0,i)

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)
        print(self.reslut_string)
            
    def MFU_FIFO(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------LRU_FIFO-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
                if len(frame)>self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
            else:
                frame.remove(i)
                frame.insert(0,i)

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)
        print(self.reslut_string)
            
    def MFU_LRU(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------MFU_LRU-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
                if len(frame)>self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
            else:
                frame.remove(i)
                frame.insert(0,i)

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)
        print(self.reslut_string)

filename = input("Enter filename : ")
filename = filename + ".txt"
with open(filename) as file_in:
    first_line = file_in.readline()
    second_line = file_in.readline()
    pm = PageManager(second_line,"3")
    pm.LRU()