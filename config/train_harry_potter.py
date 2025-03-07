# config/train_harry_potter.py

out_dir = 'out-harry_potter'
eval_interval = 500
eval_iters = 200
log_interval = 10

always_save_checkpoint = True
dataset = 'harrypotter'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 64

n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 6e-4
max_iters = 2000
lr_decay_iters = 2000
min_lr = 6e-5
beta2 = 0.99

warmup_iters = 100



# init_from = 'resume'
