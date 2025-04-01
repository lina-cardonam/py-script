import pandas as pd
from collections import OrderedDict;

df = pd.read_csv("src/files_out/MODELO.csv", sep=";")

##Read 'til SPLITTER PRIMARIO
data = df.iloc[:, :7]  

##Remove duplicates
unique_rows = list(OrderedDict.fromkeys(map(tuple, data.values)));

for row in unique_rows:
    print(row)

class InventoryObjDTOResponse:
    def __init__(self, relation, sourceParentClassName, sourceParentName, sourceClassName, sourceName, 
                targetParentClassName1, targetParentName1, targetParentClassName2, targetParentName2, targetClassName, targetName):
        self.relation = relation
        self.sourceParentClassName = sourceParentClassName
        self.sourceParentName = sourceParentName
        self.sourceClassName = sourceClassName
        self.sourceName = sourceName
        self.targetParentClassName1 = targetParentClassName1
        self.targetParentName1 = targetParentName1
        self.targetParentClassName2 = targetParentClassName2
        self.targetParentName2 = targetParentName2
        self.targetClassName = targetClassName
        self.targetName = targetName

    class Builder:
        def __init__(self):
            self._relation = None
            self._sourceParentClassName = None
            self._sourceParentName = None
            self._sourceClassName = None
            self._sourceName = None
            self._targetParentClassName1 = None
            self._targetParentName1 = None
            self._targetParentClassName2 = None
            self._targetParentName2 = None
            self._targetClassName = None
            self._targetName = None

        def relation(self, relation):
            self._relation = relation
            return self

        def sourceParentClassName(self, sourceParentClassName):
            self._sourceParentClassName = sourceParentClassName
            return self

        def sourceParentName(self, sourceParentName):
            self._sourceParentName = sourceParentName
            return self

        def sourceClassName(self, sourceClassName):
            self._sourceClassName = sourceClassName
            return self

        def sourceName(self, sourceName):
            self._sourceName = sourceName
            return self

        def targetParentClassName1(self, targetParentClassName1):
            self._targetParentClassName1 = targetParentClassName1
            return self

        def targetParentName1(self, targetParentName1):
            self._targetParentName1 = targetParentName1
            return self
        
        def targetParentClassName2(self, targetParentClassName2):
            self._targetParentClassName2 = targetParentClassName2
            return self

        def targetParentName2(self, targetParentName2):
            self._targetParentName2 = targetParentName2
            return self

        def targetClassName(self, targetClassName):
            self._targetClassName = targetClassName
            return self

        def targetName(self, targetName):
            self._targetName = targetName
            return self

        def build(self):
            return InventoryObjDTOResponse(
                self._relation, self._sourceParentClassName, self._sourceParentName, 
                self._sourceClassName, self._sourceName, self._targetParentClassName1, 
                self._targetParentName1, self._targetParentClassName2, self._targetParentName2, 
                self._targetClassName, self._targetName
            )

##Constants
RELATION = "endpointB";
PARENT_SOURCE_CLASSNAME = "WireContainer";
PARENT_SOURCE_NAME = "144F-Paita";
SOURCE_CLASSNAME = "OpticalLink";
TARGET_CLASSNAME = "OpticalPort";
TARGET_NAME = "001-IN";
CLASS_DIVICAU = "Divicau";
CLASS_SPLITTER = "FiberSplitter";

objs = [];


def format_fiber(fiber):
    num = int(fiber[1:])
    return f"F-{num:03d}"

for row in unique_rows:
    objs.append(
        InventoryObjDTOResponse.Builder()
            .relation(RELATION)
            .sourceParentClassName(PARENT_SOURCE_CLASSNAME)
            .sourceParentName(PARENT_SOURCE_NAME)
            .sourceClassName(SOURCE_CLASSNAME)
            .sourceName(format_fiber(row[4]))
            .targetParentClassName1(CLASS_DIVICAU)
            .targetParentName1(row[5])
            .targetParentClassName2(CLASS_SPLITTER)
            .targetParentName2(row[6])
            .targetClassName(TARGET_CLASSNAME)
            .targetName(TARGET_NAME)
            .build()
    );
    
headers = [
    "relation", "parentClassName", "parentName", "sourceClassName", "sourceName",
    "parentClassName", "parentName", "parentClassName", "parentName", "targetClassName", "targetName",
]

data = [
    (
        obj.relation, 
        obj.sourceParentClassName, 
        obj.sourceParentName, 
        obj.sourceClassName, 
        obj.sourceName,
        obj.targetParentClassName1, 
        obj.targetParentName1, 
        obj.targetParentClassName2, 
        obj.targetParentName2, 
        obj.targetClassName, 
        obj.targetName
    ) 
    for obj in objs
]


df = pd.DataFrame(data, columns=headers)

df.to_csv("src/files_out/CONTAINER_TO_DIVICAU.csv", index=False, encoding="utf-8", sep=";")