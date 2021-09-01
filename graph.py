import os
import tensorflow as tf
 
PRETRAINED_MODEL_PATH = './pretrained_model'
file_list = os.listdir(PRETRAINED_MODEL_PATH)
 
model_list = {}
num_model = 1
for file in file_list:
    if 'tar.gz' in file:
        continue
    
    model_list[num_model] = file
    num_model += 1
 
print('\n[ model list ]')
for key, value in model_list.items():
    print(str(key) + '.', value)
    
 
user_input = int(input('\n사용할 모델을 고르세요 : '))
model = model_list[user_input]
 
PATH_TO_FROZEN_GRAPH = PRETRAINED_MODEL_PATH + '/' + model + '/frozen_inference_graph.pb'
 
detection_graph = tf.Graph()
with detection_graph.as_default():
 
    od_graph_def = tf.GraphDef()
 
    with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as f:
 
        serialized_graph = f.read()
        od_graph_def.ParseFromString(serialized_graph)                                             
 
        tf.import_graph_def(od_graph_def, name = "")
print('\n계산 그래프 로드 완료...')