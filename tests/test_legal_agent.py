"""
Tests for Legal AI Agent
"""

import pytest
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.project2_legal_agent.tools import LegalSearchTool, ConstitutionTool, CaseLawTool


def test_legal_search_tool():
    """Test the legal search tool"""
    tool = LegalSearchTool()
    result = tool._run("freedom of speech")
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0


def test_constitution_tool():
    """Test the constitution analysis tool"""
    tool = ConstitutionTool()
    result = tool._run("Article 19")
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0


def test_case_law_tool():
    """Test the case law search tool"""
    tool = CaseLawTool()
    result = tool._run("Kesavananda Bharati")
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0


def test_tools_have_proper_attributes():
    """Test that tools have required attributes"""
    legal_tool = LegalSearchTool()
    assert hasattr(legal_tool, 'name')
    assert hasattr(legal_tool, 'description')
    assert hasattr(legal_tool, '_run')
    
    const_tool = ConstitutionTool()
    assert hasattr(const_tool, 'name')
    assert hasattr(const_tool, 'description')
    assert hasattr(const_tool, '_run')
    
    case_tool = CaseLawTool()
    assert hasattr(case_tool, 'name')
    assert hasattr(case_tool, 'description')
    assert hasattr(case_tool, '_run')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
