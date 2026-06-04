import pandas as pd
import numpy as np

from config import DATA_DIR


class DataFrameManager:

    def __init__(self):

        self.orders_df = pd.read_csv(
            DATA_DIR / "olist_orders_dataset.csv"
        )

        self.customers_df = pd.read_csv(
            DATA_DIR / "olist_customers_dataset.csv"
        )

        self.products_df = pd.read_csv(
            DATA_DIR / "olist_products_dataset.csv"
        )

        self.order_items_df = pd.read_csv(
            DATA_DIR / "olist_order_items_dataset.csv"
        )

        self.payments_df = pd.read_csv(
            DATA_DIR / "olist_order_payments_dataset.csv"
        )

        self.sellers_df = pd.read_csv(
            DATA_DIR / "olist_sellers_dataset.csv"
        )

        self._preprocess()
        
        self.tables = {
            "orders_df": self.orders_df,
            "customers_df": self.customers_df,
            "products_df": self.products_df,
            "order_items_df": self.order_items_df,
            "payments_df": self.payments_df,
            "sellers_df": self.sellers_df,
        }

    def _preprocess(self):

        # =====================================
        # Orders
        # =====================================

        delivered_orders = self.orders_df[
            self.orders_df["order_status"] == "delivered"
        ]

        bad_delivered = delivered_orders[
            delivered_orders[
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date"
                ]
            ]
            .isnull()
            .any(axis=1)
        ]

        self.orders_df = self.orders_df.drop(
            bad_delivered.index
        )

        # =====================================
        # Products
        # =====================================

        self.products_df["product_category_name"] = (
            self.products_df["product_category_name"]
            .fillna("unknown")
        )

        self.products_df["missing_catalog_metadata"] = (
            self.products_df[
                [
                    "product_name_lenght",
                    "product_description_lenght",
                    "product_photos_qty"
                ]
            ]
            .isnull()
            .all(axis=1)
        )

        self.products_df["missing_dimensions"] = (
            self.products_df[
                [
                    "product_weight_g",
                    "product_length_cm",
                    "product_height_cm",
                    "product_width_cm"
                ]
            ]
            .isnull()
            .any(axis=1)
        )

        self.products_df["data_quality_status"] = np.select(
            [
                self.products_df["missing_catalog_metadata"]
                & self.products_df["missing_dimensions"],

                self.products_df["missing_catalog_metadata"],

                self.products_df["missing_dimensions"]
            ],
            [
                "missing_catalog_and_dimensions",
                "missing_catalog",
                "missing_dimensions"
            ],
            default="complete"
        )
