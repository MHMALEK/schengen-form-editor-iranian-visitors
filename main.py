import pypdftk


# Use pypdftk to fill the form
pypdftk.fill_form(
    pdf_path="form-schengen.pdf",
    datas={"1.  Surname (Family name) (x)": "dasdas", "8": "Keuze1"},
    out_file="form-schengen-filled.pdf",
    flatten=True,
)
