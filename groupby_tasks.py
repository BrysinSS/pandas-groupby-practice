Задача B.2.b
df.groupby("brand",as_index=False).agg({"price":"mean","ssdgb":"mean"})[lambda x: x["ssdgb"]>512].sort_values("price",ascending=False).head(5)

Задача B.3.a
(df.groupby("brand",as_index=False).agg(model_count=("model_name","count"),
                                        spec_score=("spec_score","mean")).sort_values("model_count",ascending=False).head(10)
)

Задача B.4 
df.groupby("brand",as_index=False).agg({"price":"mean","spec_score":"mean"}).assign(price_per_score=lambda x:(x["price"] / x["spec_score"])).sort_values("price_per_score",ascending=True).head(5)

Задача B.5
df.groupby("brand",as_index=False).agg({"ramgb":"mean","spec_score":"mean","price":"mean"}).assign(total_value=lambda x:(x["ramgb"]*x["spec_score"] / x["price"])).sort_values("total_value", ascending=False).head(5)

Задача BZ.1
(
    df[df["ramgb"] > 8]
      .groupby("brand", as_index=False)["price"]
      .mean()
      .sort_values("price")
      .head(5)
)
BZ.2 
df.groupby("brand",as_index=False).agg({"price":"mean","spec_score":"mean"}).assign(price_per_score=lambda x:(x["price"]/x["spec_score"])).sort_values("price_per_score",ascending=False).head(5)

 BZ.3 
df[(df["ssdgb"]>512) & (df["ramgb"]>=16)].groupby("brand",as_index=False).size().reset_index(name=model_count).sort_values("model_count",ascending=False).head(5)

BZ.4
df[(df["screen_sizeinches"]>=15) & (df["ramgb"]>=16) & (df["spec_score"]>=65)].groupby("brand",as_index=False).agg({"price":"mean","spec_score":"mean","ramgb":"mean"}).assign(value_index=lambda x:(x["spec_score"]*x["ramgb"]/x["price"])).sort_values("value_index",ascending=False).head(5)
