import connexion
import six

from photo_portfolio.models.id_subpage_section_body import IdSubpageSectionBody  # noqa: E501
from photo_portfolio.models.image import Image  # noqa: E501
from photo_portfolio.models.section import Section  # noqa: E501
from photo_portfolio import util


def create_section(id_subpage, body=None):  # noqa: E501
    """creates a new section on a subpage

     # noqa: E501

    :param id_subpage: path of a subpage
    :type id_subpage: int
    :param body: 
    :type body: dict | bytes

    :rtype: Section
    """
    if connexion.request.is_json:
        body = IdSubpageSectionBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_image_from_section(id_subpage, id_section, id_image):  # noqa: E501
    """deletes an image from section

     # noqa: E501

    :param id_subpage: id of a subpage
    :type id_subpage: int
    :param id_section: id of section
    :type id_section: int
    :param id_image: id of image
    :type id_image: int

    :rtype: List[Image]
    """
    return 'do some magic!'


def delete_section_by_id(id_subpage, id_section):  # noqa: E501
    """deletes a section by ID

     # noqa: E501

    :param id_subpage: path of a subpage
    :type id_subpage: int
    :param id_section: path of a subpage
    :type id_section: int

    :rtype: None
    """
    return 'do some magic!'


def get_section_by_id(id_subpage, id_section):  # noqa: E501
    """finds a section by ID

     # noqa: E501

    :param id_subpage: path of a subpage
    :type id_subpage: int
    :param id_section: path of a subpage
    :type id_section: int

    :rtype: Section
    """
    return 'do some magic!'


def get_sections(id_subpage):  # noqa: E501
    """returns a array of sections of subpage

     # noqa: E501

    :param id_subpage: 
    :type id_subpage: int

    :rtype: List[Section]
    """
    return 'do some magic!'


def patch_image_order(body, id_subpage, id_section):  # noqa: E501
    """modifies the order of photos in section or add all photos from ID array to this section

     # noqa: E501

    :param body: Order of elements in container
    :type body: List[]
    :param id_subpage: id of a subpage
    :type id_subpage: int
    :param id_section: id of section
    :type id_section: int

    :rtype: List[Image]
    """
    return 'do some magic!'


def patch_section_order(body, id_subpage):  # noqa: E501
    """modifies the order of sections in subpage

     # noqa: E501

    :param body: Order of elements in container
    :type body: List[]
    :param id_subpage: path of a subpage
    :type id_subpage: int

    :rtype: List[Section]
    """
    return 'do some magic!'


def patch_section_value(id_subpage, id_section, body=None):  # noqa: E501
    """modifies a value of section

    modifies a value of section - new value object does not replace old, but method combines both of them (@see patch method) # noqa: E501

    :param id_subpage: id of a subpage
    :type id_subpage: int
    :param id_section: id of section
    :type id_section: int
    :param body: value of section
    :type body: dict | bytes

    :rtype: Section
    """
    if connexion.request.is_json:
        body = Dict.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_image_to_section(id_subpage, id_section, value):  # noqa: E501
    """add one image to a section

     # noqa: E501

    :param id_subpage: id of a subpage
    :type id_subpage: int
    :param id_section: id of section
    :type id_section: int
    :param value: id of image
    :type value: int

    :rtype: List[Image]
    """
    return 'do some magic!'
