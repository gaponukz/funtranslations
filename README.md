# funtranslations

`FunTranslations` gives access to the full set of translations available at funtranslations.com so that you can integrate them in your workflow or an app.
## [List of api](https://funtranslations.com/api/)

```python
from funtranslations import FunTranslation

translation = FunTranslation("yoda")
print(translation.translate("what do you think about me?"))
```

## Requirements

* python >= 3.8
* `dict2object-gaponukz==0.0.2`