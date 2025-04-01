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
                 targetParentClassName, targetParentName, targetClassName, targetName):
        self.relation = relation
        self.sourceParentClassName = sourceParentClassName
        self.sourceParentName = sourceParentName
        self.sourceClassName = sourceClassName
        self.sourceName = sourceName
        self.targetParentClassName = targetParentClassName
        self.targetParentName = targetParentName
        self.targetClassName = targetClassName
        self.targetName = targetName

    class Builder:
        def __init__(self):
            self._relation = None
            self._sourceParentClassName = None
            self._sourceParentName = None
            self._sourceClassName = None
            self._sourceName = None
            self._targetParentClassName = None
            self._targetParentName = None
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

        def targetParentClassName(self, targetParentClassName):
            self._targetParentClassName = targetParentClassName
            return self

        def targetParentName(self, targetParentName):
            self._targetParentName = targetParentName
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
                self._sourceClassName, self._sourceName, self._targetParentClassName, 
                self._targetParentName, self._targetClassName, self._targetName
            )

##Constants
RELATION = "endpointA";
PARENT_SOURCE_CLASSNAME = "ODF";
SOURCE_CLASSNAME = "OpticalPort";
PARENT_TARGET_CLASSNAME = "WireContainer";
PARENT_TARGET_NAME = "144F-Paita";
TARGET_CLASSNAME = "OpticalLink";

objs = [];

def format_port(port):
    num = int(port[1:])
    return f"{num:03d}-OUT"

def format_fiber(fiber):
    num = int(fiber[1:])
    return f"F-{num:03d}"

for row in unique_rows:
    objs.append(
        InventoryObjDTOResponse.Builder()
            .relation(RELATION)
            .sourceParentClassName(PARENT_SOURCE_CLASSNAME)
            .sourceParentName(row[0])
            .sourceClassName(SOURCE_CLASSNAME)
            .sourceName(format_port(row[1]))
            .targetParentClassName(PARENT_TARGET_CLASSNAME)
            .targetParentName(PARENT_TARGET_NAME)
            .targetClassName(TARGET_CLASSNAME)
            .targetName(format_fiber(row[4]))
            .build()
    );
    
headers = [
    "relation", "parentClassName", "parentName", "sourceClassName", "sourceName",
    "parentClassName", "parentName", "targetClassName", "targetName",
]

data = [(
    obj.relation, obj.sourceParentClassName, obj.sourceParentName, obj.sourceClassName, obj.sourceName,
    obj.targetParentClassName, obj.targetParentName, obj.targetClassName, obj.targetName
) for obj in objs]


df = pd.DataFrame(data, columns=headers)

df.to_csv("src/files_out/ODF_TO_CONTAINER.csv", index=False, encoding="utf-8", sep=";")