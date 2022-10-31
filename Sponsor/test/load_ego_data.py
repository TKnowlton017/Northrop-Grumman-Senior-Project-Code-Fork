from l5kit.rasterization import build_rasterizer
from l5kit.configs import load_config_data
from l5kit.data import LocalDataManager, ChunkedDataset
from l5kit.dataset import EgoDataset

zarr_dt = ChunkedDataset("/prediction-sample-dataset/scenes/sample.zarr")
zarr_dt.open()

# additional information is required for rasterisation
cfg = load_config_data("./agent_motion_config.yaml")
rast = build_rasterizer(cfg, LocalDataManager(None))

dataset = EgoDataset(cfg, zarr_dt, rast)
for data in dataset:  # this iterates over frames under the hood
    print(data["target_positions"])
    print(data["history_positions"])