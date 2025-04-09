import pandas as pd
from collections import OrderedDict;

df = pd.read_csv("/home/lcardona/projects/mi-fibra/py-script/src/files_out_1/CONEXIONES CB-D01.csv", sep=";")

data = df.iloc[:, :] 

##Remove duplicates
unique_rows = list(OrderedDict.fromkeys(map(tuple, data.values)));

for row in unique_rows:
    print(row)

class InventoryObjDTOResponse:
    def __init__(self, relation, sourceParentClassName1, sourceParentName1, sourceParentClassName2, sourceParentName2, 
                 sourceClassName, sourceName, targetParentClassName1, targetParentName1, targetParentClassName2, 
                 targetParentName2, targetClassName, targetName):
        self.relation = relation
        self.sourceParentClassName1 = sourceParentClassName1
        self.sourceParentName1 = sourceParentName1
        self.sourceParentClassName2 = sourceParentClassName2
        self.sourceParentName2 = sourceParentName2
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
            self._sourceParentClassName1 = None
            self._sourceParentName1 = None
            self._sourceParentClassName2 = None
            self._sourceParentName2 = None
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

        def sourceParentClassName1(self, sourceParentClassName1):
            self._sourceParentClassName1 = sourceParentClassName1
            return self

        def sourceParentName1(self, sourceParentName1):
            self._sourceParentName1 = sourceParentName1
            return self

        def sourceParentClassName2(self, sourceParentClassName2):
            self._sourceParentClassName2 = sourceParentClassName2
            return self

        def sourceParentName2(self, sourceParentName2):
            self._sourceParentName2 = sourceParentName2
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
                self._relation, self._sourceParentClassName1, self._sourceParentName1,
                self._sourceParentClassName2, self._sourceParentName2, self._sourceClassName, self._sourceName,
                self._targetParentClassName1, self._targetParentName1, self._targetParentClassName2,
                self._targetParentName2, self._targetClassName, self._targetName
            )

##Constants
RELATION = "endpointB";

PARENT_SOURCE_CLASSNAME_1 = "Distrito";
PARENT_SOURCE_NAME_1 = "Chimbote";
PARENT_SOURCE_CLASSNAME_2 = "WireContainer";
SOURCE_CLASSNAME = "OpticalLink";

PARENT_TARGET_CLASSNAME_1 = "NAP";
PARENT_TARGET_CLASSNAME_2 = "FiberSplitter";
TARGET_CLASSNAME = "OpticalPort";
TARGET_NAME = "001-IN";

objs = [];

def format_fiber(fiber):
    num = int(fiber[1:])
    return f"F-{num:03d}"

for row in unique_rows:
    aux = row[0][:2]
    num = int(row[0][2:])
    zoneNum = aux + " " + f"{num:03d}"
    splittAux = row[6].split("D")[1]
    objs.append(
        InventoryObjDTOResponse.Builder()
            .relation(RELATION)
            .sourceParentClassName1(PARENT_SOURCE_CLASSNAME_1)
            .sourceParentName1(PARENT_SOURCE_NAME_1)
            .sourceParentClassName2(PARENT_SOURCE_CLASSNAME_2)
            .sourceParentName2(str(row[8]) + "-" + str(row[9]))
            .sourceClassName(SOURCE_CLASSNAME)
            .sourceName(format_fiber(row[10]))
            .targetParentClassName1(PARENT_TARGET_CLASSNAME_1)
            .targetParentName1(zoneNum + "-" + row[5] + "-" + f"{int(row[11]):02d}")
            .targetParentClassName2(PARENT_TARGET_CLASSNAME_2)
            .targetParentName2(row[12])
            .targetClassName(TARGET_CLASSNAME)
            .targetName(TARGET_NAME)
            .build()
    );
    
headers = [
    "relation", "parentClassName", "parentName", "parentClassNameOfSpecial", "parentNameOfSpecial", "sourceClassName", "sourceName",
    "parentClassName", "parentName", "parentClassName", "parentName", "targetClassName", "targetName",
]

data = [
    (
        obj.relation, 
        obj.sourceParentClassName1, 
        obj.sourceParentName1,
        obj.sourceParentClassName2,
        obj.sourceParentName2, 
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

df.to_csv("src/files_out_1/CONTAINER_NAP.csv", index=False, encoding="utf-8", sep=";")